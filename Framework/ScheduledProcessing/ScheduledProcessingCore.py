# This file is part of "ZScan Processor".
#
# "ZScan Processor" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "ZScan Processor" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "ZScan Processor".  If not, see <http://www.gnu.org/licenses/>.

#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging
import cv2
from datetime import datetime
import os

# Custom imports
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI
from Resources import Constants

from Framework.DetectionProcessing import DetectionProcessorCore

#####################################
# Global Variables
#####################################
CAP_A_OFFSET = 65
WELL_COMPRESSION_LEVEL = 0
PLATE_COMPRESSION_LEVEL = 6
FAILED_COMPRESSION_LEVEL = 0


#####################################
# PreviewProcessor Definition
#####################################
class ScheduleProcessor(QtCore.QThread):
    def __init__(self, shared_objects):
        super(ScheduleProcessor, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## References to GUI Elements ##########
        self.main_tab_widget = self.main_screen.main_tab_widget  # type: QtWidgets.QTabWidget

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########

        # ########## Setup program start signal connections ##########
        self.setup_signals()

    def run(self):
        self.logger.debug("Schedule Processor Thread Starting...")

        while self.run_thread_flag:
            self.check_and_run_scheduled_processes()
            self.msleep(10)

        self.logger.debug("Schedule Processor Thread Stopping...")

    def check_and_run_scheduled_processes(self):
        main_tab_not_on_settings = self.main_tab_widget.currentWidget().objectName() != "settings_tab"

        if main_tab_not_on_settings:
            if self.is_time_to_transfer():
                pass  # Do transfer stuff here
            else:
                self.check_for_new_files_and_process()

    def is_time_to_transfer(self):
        return False

    def check_for_new_files_and_process(self):
        input_path = self.settings.value("file_and_transfer_settings/input_images_path", type=str)

        for root, directories, files in os.walk(input_path):
            for filename in files:
                self.process_full_scan_from_path(os.path.join(root, filename))

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
                self.process_barcoded_plate_into_output_folder(top_plate_image, "top", top_barcode, path)
            else:
                self.logger.warning("Failed to detect top barcode for image with path \"%s\". Moving to failed." % path)
                self.process_failed_plate(top_plate_image, "top", path)

            if bottom_barcode:
                self.logger.info("Found bottom barcode with value %s. Processing outputs." % bottom_barcode)
                self.process_barcoded_plate_into_output_folder(bottom_plate_image, "bottom", bottom_barcode, path)
            else:
                self.logger.warning(
                    "Failed to detect bottom barcode for image with path \"%s\". Moving to failed." % path)
                self.process_failed_plate(bottom_plate_image, "bottom", path)

            # ##### Remove original image if everything was successful #####
            if top_barcode and bottom_barcode:
                os.unlink(path)
            else:
                self.backup_original_on_failure(path)

        except Exception as e:
            self.logger.exception("Detection process failed" % path)

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

        if not os.path.exists(wells_folder_path):
            os.mkdir(root_barcode_folder_path)

        if not os.path.exists(wells_folder_path):
            os.mkdir(wells_folder_path)

        if not os.path.exists(full_plate_folder_path):
            os.mkdir(full_plate_folder_path)

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

                cv2.imwrite(well_path, cv2.cvtColor(well_image, cv2.COLOR_RGB2BGR),
                            [cv2.IMWRITE_PNG_COMPRESSION, WELL_COMPRESSION_LEVEL])

        # Save compressed version of plate image
        compressed_full_plate_path = "%s/%s_%s.png" % (full_plate_folder_path, iso_datetime_string, barcode)
        cv2.imwrite(compressed_full_plate_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR),
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

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        pass

    def on_kill_threads__slot(self):
        self.run_thread_flag = False

    def setup_signals(self):
        self.core_signals["start"].connect(self.start)
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)
