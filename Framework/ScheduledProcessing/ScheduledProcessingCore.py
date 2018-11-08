#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from datetime import datetime, timedelta
import os
import time
import shutil
import pymysql.cursors

# Custom imports
from Framework.TrayNotifier.TrayNotifierCore import TrayNotifier
from Resources import Constants

from Framework.DetectionProcessing import DetectionProcessorCore

#####################################
# Global Variables
#####################################
STARTUP_INITIAL_DELAY = 5000  # Milli-seconds

SETTINGS_WARNING_DELAY = 300  # Seconds

CAP_A_OFFSET = 65
WELL_COMPRESSION_LEVEL = 0
PLATE_COMPRESSION_LEVEL = 6
FAILED_COMPRESSION_LEVEL = 0

NO_PLATE_MEAN_THRESHOLD = 235

MODIFICATION_DELAY_TO_PROCESS = 10  # Seconds
TRANSFER_VALID_FUTURE_WINDOW = 10  # Seconds

NO_PATH_STRING = "*** No Path Set ***"

REPLACEMENT_MAPPING = {
    "plate_id": "%PID",
    "creation_date": "%CD"
}


#####################################
# PreviewProcessor Definition
#####################################
class ScheduleProcessor(QtCore.QThread):
    set_main_tab_widget_enabled__signal = QtCore.pyqtSignal(bool)

    def __init__(self, shared_objects):
        super(ScheduleProcessor, self).__init__()

        # ########## References to shared objects and gui elements ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]
        self.tray_notifier = self.shared_objects["regular_classes"]["Tray Notifier"]  # type: TrayNotifier

        self.main_tab_widget = self.main_screen.main_tab_widget  # type: QtWidgets.QTabWidget
        self.input_images_line_edit = self.main_screen.file_transfer_input_images_line_edit  # type: QtWidgets.QLineEdit
        self.failed_rename_line_edit = self.main_screen.file_transfer_failed_rename_images_line_edit  # type: QtWidgets.QLineEdit
        self.local_output_line_edit = self.main_screen.file_transfer_local_output_line_edit  # type: QtWidgets.QLineEdit
        self.network_transfer_line_edit = self.main_screen.file_transfer_network_transfer_line_edit  # type: QtWidgets.QLineEdit
        self.transfer_time_time_edit = self.main_screen.file_transfer_transfer_time_edit  # type: QtWidgets.QTimeEdit

        self.plate_line_edits = [self.input_images_line_edit, self.failed_rename_line_edit,
                                 self.local_output_line_edit, self.network_transfer_line_edit]

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########
        self.last_warning_shown_time = 0
        self.watched_files = {}
        self.next_transfer_time = datetime.now() - timedelta(days=1)  # Set in the past to get startup logic to work
        self.transfer_attempted = True

        self.output_database = None
        self.database_cursor = None

        # ########## Setup program start signal connections ##########
        self.setup_signals()

    def run(self):
        self.msleep(STARTUP_INITIAL_DELAY)  # Used so you can change settings after initial startup
        self.logger.debug("Schedule Processor Thread Starting...")

        while self.run_thread_flag:
            self.check_and_run_scheduled_processes()
            self.msleep(10000)

        self.logger.debug("Schedule Processor Thread Stopping...")

    def check_and_run_scheduled_processes(self):
        main_tab_on_logs = self.main_tab_widget.currentWidget().objectName() == "logs_tab"
        app_hidden = self.main_screen.isHidden()

        plate_locations_valid = True
        for line_edit in self.plate_line_edits:
            if line_edit.text() == NO_PATH_STRING:
                plate_locations_valid = False
                break

        if main_tab_on_logs or app_hidden:
            if plate_locations_valid:
                self.set_main_tab_widget_enabled__signal.emit(False)

                if self.is_time_to_transfer():
                    self.do_network_transfer()
                else:
                    self.check_for_new_files_and_process()

                self.set_main_tab_widget_enabled__signal.emit(True)
            else:
                if (time.time() - self.last_warning_shown_time) > SETTINGS_WARNING_DELAY:
                    self.logger.warning("Cannot process as paths have not been set. Please enter valid paths.")
                    self.last_warning_shown_time = time.time()

    def is_time_to_transfer(self):
        # Get transfer time
        network_transfer_time_string = self.settings.value("file_and_transfer_settings/network_transfer_time", type=str)
        network_transfer_time = datetime.strptime(network_transfer_time_string, "%I:%M %p").time()

        # Check if date is the same, if not, update next transfer time to one for the current day, reset flags
        current_date = datetime.now().date()
        if current_date != self.next_transfer_time.date():
            self.next_transfer_time = datetime.combine(current_date, network_transfer_time)
            self.transfer_attempted = False

        # If next_transfer + offset > now > next transfer time AND not already_run, run transfer, set already_run
        end_valid_window_datetime = self.next_transfer_time + timedelta(seconds=TRANSFER_VALID_FUTURE_WINDOW)
        start_valid_window_datetime = self.next_transfer_time
        current_datetime = datetime.now()

        in_valid_transfer_window = start_valid_window_datetime <= current_datetime <= end_valid_window_datetime

        if in_valid_transfer_window and not self.transfer_attempted:
            self.transfer_attempted = True
            return True

        return False

    def do_network_transfer(self):
        try:
            local_output_path = self.settings.value("file_and_transfer_settings/local_output_path", type=str)
            network_path = self.settings.value("file_and_transfer_settings/network_transfer_path", type=str)

            # Make destination files/folders overwriting if needed, unlink transferred files
            self.logger.info("Beginning network transfer.")
            self.tray_notifier.show_informational_message("Network transfer started!")

            self.copy_files(local_output_path, network_path)

            self.logger.info("Network transfer finished.")
            self.tray_notifier.show_informational_message("Network transfer complete!")

            # Clear empty local directories as needed
            self.delete_empty_folders(local_output_path, delete_path_itself=False)
        except Exception as e:
            self.logger.exception("Network transfer failed!")
            self.tray_notifier.show_failure_message("Network transfer failed!")

    def copy_files(self, source, destination):
        for root, directories, files in os.walk(source):
            destination_dir = root.replace(source, destination)

            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)

            for file_to_transfer in files:
                source_path = os.path.join(root, file_to_transfer)
                destination_path = os.path.join(destination_dir, file_to_transfer)

                if os.path.exists(destination_path):
                    os.remove(destination_path)

                shutil.copy2(source_path, destination_path)

                if os.path.exists(destination_path):
                    self.logger.info("Transferred %s to %s." % (file_to_transfer, destination_dir))
                    os.unlink(source_path)

    def delete_empty_folders(self, path, delete_path_itself=True):
        items_in_root = os.listdir(path)
        for item_path in items_in_root:
            full_path = os.path.join(path, item_path)

            if os.path.isdir(full_path):
                self.delete_empty_folders(full_path)

        items_in_root = os.listdir(path)
        if len(items_in_root) == 0 and delete_path_itself:
            os.rmdir(path)

    def check_for_new_files_and_process(self):
        valid_files = self.find_files_ready_to_process()

        for file in valid_files:
            self.process_full_scan_from_path(file)

        if self.database_cursor:
            self.database_cursor.close()

        if self.output_database:
            self.output_database.close()

        self.output_database = None
        self.database_cursor = None

    def process_full_scan_from_path(self, path):
        try:
            self.logger.info("Attempting to process image with path \"%s\"" % path)

            # ##### Get full plate image and realign #####
            full_plate_image = cv2.imread(path)
            full_plate_image = cv2.cvtColor(full_plate_image, cv2.COLOR_BGR2RGB)
            full_plate_image = cv2.rotate(full_plate_image, 0)
            full_plate_image = cv2.flip(full_plate_image, 0)

            # ##### Get individual plate images #####
            top_plate_image = self.get_plate_image(full_plate_image, "top")
            bottom_plate_image = self.get_plate_image(full_plate_image, "bottom")

            # ##### Detect barcodes for plates #####
            top_barcode = self.detect_barcode(top_plate_image, "top")
            bottom_barcode = self.detect_barcode(bottom_plate_image, "bottom")

            # ##### Handle successful and failed barcode reads #####
            if top_barcode:
                self.logger.info("Found top barcode with value %s. Processing outputs." % top_barcode)
                self.tray_notifier.show_informational_message("Processing %s." % top_barcode)
                self.process_barcoded_plate_into_output_folder(top_plate_image, "top", top_barcode, path)
                self.write_plate_id_to_database(top_barcode, path)
            else:
                self.logger.warning("Failed to detect top barcode for image with path \"%s\". Moving to failed." % path)
                self.process_failed_plate(top_plate_image, "top", path)

            if bottom_barcode:
                self.logger.info("Found bottom barcode with value %s. Processing outputs." % bottom_barcode)
                self.tray_notifier.show_informational_message("Processing %s." % bottom_barcode)
                self.process_barcoded_plate_into_output_folder(bottom_plate_image, "bottom", bottom_barcode, path)
                self.write_plate_id_to_database(bottom_barcode, path)
            else:
                self.logger.warning(
                    "Failed to detect bottom barcode for image with path \"%s\". Moving to failed." % path)
                self.process_failed_plate(bottom_plate_image, "bottom", path)

            # ##### Remove original image if everything was successful #####
            should_unlink = False

            if top_barcode and bottom_barcode:
                should_unlink = True

            elif not top_barcode and not bottom_barcode:
                top_plate_mean = cv2.mean(top_plate_image)[0]
                bottom_plate_mean = cv2.mean(bottom_plate_image)[0]

                if top_plate_mean > NO_PLATE_MEAN_THRESHOLD and bottom_plate_mean > NO_PLATE_MEAN_THRESHOLD:
                    should_unlink = True

            elif not top_barcode:
                top_plate_mean = cv2.mean(top_plate_image)[0]

                if top_plate_mean > NO_PLATE_MEAN_THRESHOLD:
                    should_unlink = True

            elif not bottom_barcode:
                bottom_plate_mean = cv2.mean(bottom_plate_image)[0]

                if bottom_plate_mean > NO_PLATE_MEAN_THRESHOLD:
                    should_unlink = True

            if should_unlink:
                os.unlink(path)
            else:
                self.backup_original_on_failure(path)

        except Exception as e:
            self.logger.exception("Detection processing failed for path: " % path)
            self.tray_notifier.show_failure_message("Detection processing failed!")

    def process_barcoded_plate_into_output_folder(self, image, top_or_bottom, barcode, combined_path):
        # Get pertinent settings
        output_path = self.settings.value("file_and_transfer_settings/local_output_path", type=str)

        a1_x_location = self.settings.value("gui_elements/%s_a1_x_spinbox" % top_or_bottom, type=int)
        a1_y_location = self.settings.value("gui_elements/%s_a1_y_spinbox" % top_or_bottom, type=int)
        h12_x_location = self.settings.value("gui_elements/%s_h12_x_spinbox" % top_or_bottom, type=int)
        h12_y_location = self.settings.value("gui_elements/%s_h12_y_spinbox" % top_or_bottom, type=int)
        well_radius = self.settings.value("gui_elements/%s_well_radius_spinbox" % top_or_bottom, type=int)

        num_rows = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["rows"]
        num_columns = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["columns"]

        # Get creation time for the original image (ISO 8601 format)
        iso_datetime_string = datetime.fromtimestamp(os.path.getctime(combined_path)).strftime("%Y%m%dT%H%M%S")

        # Make new folder with barcode name and folder for wells
        root_barcode_folder_path = output_path + "/" + barcode
        wells_folder_path = root_barcode_folder_path + "/wells"
        full_plate_folder_path = root_barcode_folder_path + "/full_plate"

        for path in [root_barcode_folder_path, wells_folder_path, full_plate_folder_path]:
            if not os.path.exists(path):
                os.mkdir(path)

        # Make backup copy of main input image so we can save a clean version
        image_untouched = image.copy()

        # Split plate into named wells and save
        offset_per_well_x = (h12_x_location - a1_x_location) / (num_columns - 1)
        offset_per_well_y = (h12_y_location - a1_y_location) / (num_rows - 1)

        for x in range(num_columns):
            for y in range(num_rows):
                x_location = int(a1_x_location + (x * offset_per_well_x))
                y_location = int(a1_y_location + (y * offset_per_well_y))

                well_name = "%s_%s_%s%02d.png" % (iso_datetime_string, barcode, chr(CAP_A_OFFSET + y), x + 1)
                well_path = wells_folder_path + "/" + well_name
                well_image = image[(y_location - well_radius):(y_location + well_radius),
                             (x_location - well_radius):(x_location + well_radius)]
                self.draw_barcode_overlay(well_image, barcode, top_or_bottom, "well")

                cv2.imwrite(well_path, cv2.cvtColor(well_image, cv2.COLOR_RGB2BGR),
                            [cv2.IMWRITE_PNG_COMPRESSION, WELL_COMPRESSION_LEVEL])

        # Save compressed version of plate image
        compressed_full_plate_path = "%s/%s_%s.png" % (full_plate_folder_path, iso_datetime_string, barcode)
        self.draw_barcode_overlay(image_untouched, barcode, top_or_bottom, "plate")
        cv2.imwrite(compressed_full_plate_path, cv2.cvtColor(image_untouched, cv2.COLOR_RGB2BGR),
                    [cv2.IMWRITE_PNG_COMPRESSION, PLATE_COMPRESSION_LEVEL])

    def process_failed_plate(self, image, top_or_bottom, combined_path):
        # Get pertinent settings
        failed_path = self.settings.value("file_and_transfer_settings/failed_rename_path", type=str)

        # Get creation time for the original image (ISO 8601 format)
        iso_datetime_string = datetime.fromtimestamp(os.path.getctime(combined_path)).strftime("%Y%m%dT%H%M%S")

        # Save the failed image
        failed_image_name = "%s/%s_%s_individual.png" % (failed_path, iso_datetime_string, top_or_bottom)

        cv2.imwrite(failed_image_name, cv2.cvtColor(image, cv2.COLOR_RGB2BGR),
                    [cv2.IMWRITE_PNG_COMPRESSION, FAILED_COMPRESSION_LEVEL])

    def backup_original_on_failure(self, path):
        # Get pertinent settings
        failed_path = self.settings.value("file_and_transfer_settings/failed_rename_path", type=str)

        # Get creation time for the original image (ISO 8601 format)
        iso_datetime_string = datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y%m%dT%H%M%S")

        # Save the failed image
        failed_image_name = "%s/%s_original.tif" % (failed_path, iso_datetime_string)

        os.rename(path, failed_image_name)

    def find_files_ready_to_process(self):
        # Get pertinent settings
        input_path = self.settings.value("file_and_transfer_settings/input_images_path", type=str)

        all_files = []

        # Get all files
        for root, directories, files in os.walk(input_path):
            for filename in files:
                file_path = os.path.join(root, filename)

                all_files.append(file_path)

                if file_path not in self.watched_files:
                    self.watched_files[file_path] = time.time()

        # Remove any files from watch that are no longer present
        dead_files = [file for file in self.watched_files.keys() if file not in all_files]
        for dead_file in dead_files:
            del self.watched_files[dead_file]

        # Go through files, build new list of all files that haven't had a file lock in a long time
        files_valid_to_process = []

        for file_path, last_write_attempt in self.watched_files.items():
            try:
                os.rename(file_path, file_path)
            except OSError:
                self.watched_files[file_path] = time.time()

            if (time.time() - last_write_attempt) > MODIFICATION_DELAY_TO_PROCESS:
                files_valid_to_process.append(file_path)

        # Return the new list
        return files_valid_to_process

    def detect_barcode(self, image, top_or_bottom):
        processing_dictionary = {
            "scan_box_image": self.get_barcode_scanbox_image(image, top_or_bottom),

            "barcode_x_size": self.settings.value("gui_elements/%s_barcode_x_size_spinbox" % top_or_bottom, type=int),
            "barcode_y_size": self.settings.value("gui_elements/%s_barcode_y_size_spinbox" % top_or_bottom, type=int),

            "threshold_center": self.settings.value("gui_elements/%s_threshold_center_spinbox" % top_or_bottom,
                                                    type=int),
            "threshold_range": self.settings.value("gui_elements/%s_threshold_range_spinbox" % top_or_bottom, type=int),
        }

        detection_processor = DetectionProcessorCore.DetectionProcessor(processing_dictionary)
        detection_processor.process()

        if detection_processor.bardcode_found():
            barcode_data = detection_processor.get_barcode_data()["barcode_value"]
        else:
            barcode_data = None

        detection_processor.cleanup()

        return barcode_data

    def get_plate_image(self, image, top_or_bottom):
        plate_split_line_location = self.settings.value("gui_elements/alignment_shared_split_line_spinbox", type=int)

        preview_image = image
        height, width, _ = preview_image.shape

        if top_or_bottom == "top":
            return preview_image[0:height, 0:plate_split_line_location].copy()
        elif top_or_bottom == "bottom":
            return preview_image[0:height, plate_split_line_location:width].copy()

    def get_barcode_scanbox_image(self, image, top_or_bottom):
        scanbox_x_position_spinbox = self.settings.value("gui_elements/%s_scanbox_x_position_spinbox" % top_or_bottom,
                                                         type=int)
        scanbox_y_position_spinbox = self.settings.value("gui_elements/%s_scanbox_y_position_spinbox" % top_or_bottom,
                                                         type=int)
        scanbox_x_size_spinbox = self.settings.value("gui_elements/%s_scanbox_x_size_spinbox" % top_or_bottom, type=int)
        scanbox_y_size_spinbox = self.settings.value("gui_elements/%s_scanbox_y_size_spinbox" % top_or_bottom, type=int)

        pt1_x = scanbox_x_position_spinbox - (scanbox_x_size_spinbox // 2)
        pt1_y = scanbox_y_position_spinbox - (scanbox_y_size_spinbox // 2)

        pt2_x = scanbox_x_position_spinbox + (scanbox_x_size_spinbox // 2)
        pt2_y = scanbox_y_position_spinbox + (scanbox_y_size_spinbox // 2)

        return image[pt1_y:pt2_y, pt1_x:pt2_x].copy()

    def draw_barcode_overlay(self, image, text, top_or_bottom, plate_or_well):
        font_size = self.settings.value("gui_elements/%s_overlay_%s_font_size_spinbox" % (top_or_bottom, plate_or_well),
                                        type=int)
        try:
            font = ImageFont.truetype("Roboto-Regular.ttf", font_size)

            barcode_image = Image.new('RGB', (1, 1), (0, 0, 0))
            image_draw = ImageDraw.Draw(barcode_image)

            width, height = image_draw.textsize(text, font)
            width_offset, height_offset = font.getoffset(text)

            barcode_image = Image.new('RGB', (width + width_offset, height + height_offset), (0, 0, 0))
            image_draw = ImageDraw.Draw(barcode_image)
            image_draw.text((0, 0), text, font=font)

            width, height = barcode_image.size

            overlay_image = np.array(barcode_image)
            image[0:height, 0:width] = overlay_image
        except Exception as e:
            self.logger.exception("Barcode overlay failed... Please check settings...")

    def write_plate_id_to_database(self, plate_id, plate_path):
        host = self.settings.value("gui_elements/database_host_line_edit", type=str)
        username = self.settings.value("gui_elements/database_username_line_edit", type=str)
        password = self.settings.value("gui_elements/database_password_line_edit", type=str)
        database = self.settings.value("gui_elements/database_database_line_edit", type=str)
        date_format = self.settings.value("gui_elements/database_date_format_line_edit", type=str)
        query = self.settings.value("gui_elements/database_query_line_edit", type=str)

        formatted_creation_date = datetime.fromtimestamp(os.path.getctime(plate_path)).strftime(date_format)

        try:
            if not self.output_database:
                self.output_database = pymysql.connect(
                    host=host,
                    user=username,
                    password=password,
                    db=database
                )

                self.database_cursor = self.output_database.cursor()

            # Replace plate id
            query = query.replace(REPLACEMENT_MAPPING["plate_id"], plate_id)

            # Fill in date
            query = query.replace(REPLACEMENT_MAPPING["creation_date"], formatted_creation_date)

            # Execute SQL command, commit DB
            self.database_cursor.execute(query)
            self.output_database.commit()

            # Notify and log based on success
            if self.database_cursor.rowcount == 0:
                self.tray_notifier.show_failure_message(
                    "Write of plate \"%s\" to database \"%s\" did not affect any rows!" % (plate_id, database))
                self.logger.warning(
                    "Write of plate \"%s\" to database \"%s\" did not affect any rows!" % (plate_id, database))
            else:
                self.tray_notifier.show_informational_message(
                    "Wrote plate \"%s\" to database \"%s\" affecting %d rows." % (
                        plate_id, database, self.database_cursor.rowcount))
                self.logger.info("Wrote plate \"%s\" to database \"%s\" affecting %d rows." % (
                    plate_id, database, self.database_cursor.rowcount))

        except pymysql.Error as e:
            if self.database_cursor:
                self.database_cursor.close()

            if self.output_database:
                self.output_database.close()

            self.output_database = None
            self.database_cursor = None

            self.tray_notifier.show_failure_message(
                "Write of plate \"%s\" to database \"%s\" failed! Please check DB settings!" % (plate_id, database))
            self.logger.warning(
                "Write of plate \"%s\" to database \"%s\" failed! Please check DB settings! Error: %s" % (
                    plate_id, database, e.args[1]))

    def on_transfer_timeedit_changed__slot(self):
        self.next_transfer_time = datetime.now() - timedelta(days=1)  # Set in the past to reset valid transfer

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        self.set_main_tab_widget_enabled__signal.connect(self.main_tab_widget.setEnabled)
        self.transfer_time_time_edit.timeChanged.connect(self.on_transfer_timeedit_changed__slot)

    def on_kill_threads__slot(self):
        self.run_thread_flag = False

    def setup_signals(self):
        self.core_signals["start"].connect(self.start)
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)
