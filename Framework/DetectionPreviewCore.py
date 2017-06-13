"""
    This file contains the detection preview sub-class
"""

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
import subprocess
import cv2
import qimage2ndarray
from os.path import exists
from os import makedirs

# Custom Import
from Framework import WorkerCore

#####################################
# Global Variables
#####################################
# Settings for imports
# Image.MAX_IMAGE_PIXELS = None  # This disables the decompression bomb warning


UI_PREVIEW_LOAD_IMAGE_MAIN_PATH = "Resources/UI/preview_please_load_image_main.png"
UI_PREVIEW_LOAD_IMAGE_BC_PATH = "Resources/UI/preview_please_load_image_barcode.png"

UI_PREVIEW_MAIN_LB_WIDTH = 280
UI_PREVIEW_MAIN_LB_HEIGHT = 830

UI_PREVIEW_BC_WIDTH = WorkerCore.UI_PREVIEW_BC_WIDTH
UI_PREVIEW_BC_HEIGHT = WorkerCore.UI_PREVIEW_BC_HEIGHT

PLATE_ROWS = 12
PLATE_COLS = 8

PLATE_SPLIT_COLOR = (0, 0, 255)  # BGR -> Full Red
PLATE_LINE_THICKNESS = 150

TOP_WELL_COLOR = (0, 128, 0)  # BGR -> Dark Green
TOP_WELL_GRID_COLOR = (0, 255, 0)  # BGR -> Full Green
BOTTOM_WELL_COLOR = (255, 0, 0)  # BGR -> Navy Blue
BOTTOM_WELL_GRID_COLOR = (255, 191, 0)  # BGR -> Sky Blue
WELL_CIRCLE_THICKNESS = 100
WELL_CIRCLE_RADIUS = 360

SCAN_BOX_THICKNESS = 150
SCAN_BOX_COLOR = (72, 124, 247)

BC_BOX_THICKNESS = 100
BC_BOX_COLOR = (88, 83, 237)

DETECT_ALL_Y_INCREMENT = 50
DETECT_ALL_X_INCREMENT = 300


#####################################
# Detection Preview Class Definition
#####################################
class DetectionPreview(QtCore.QThread):
    preview_images_ready_signal = QtCore.pyqtSignal()

    def __init__(self, main_window):
        super(DetectionPreview, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window  # type: QtWidgets.QMainWindow

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########
        self.detection_settings_tab_open = False

        self.detection_main_preview_pixmap = None

        self.detection_top_bc_raw_preview_pixmap = None
        self.detection_top_bc_threshold_preview_pixmap = None
        self.detection_top_bc_string = "Not Found"

        self.detection_bottom_bc_raw_preview_pixmap = None
        self.detection_bottom_bc_threshold_preview_pixmap = None
        self.detection_bottom_bc_string = "Not Found"

        self.detection_image_updates_needed = False

        self.barcode_found = False

        # ########## Load class settings ##########
        self.__load_settings()

    def run(self):
        self.logger.debug("Detection Preview Thread Starting...")
        while self.run_thread_flag:
            if self.detection_settings_tab_open:
                self.__show_detection_settings_preview()
            self.msleep(100)

        self.logger.debug("Detection Preview Thread Stopping...")

    def __load_settings(self):
        pass

    # noinspection PyUnresolvedReferences
    def connect_signals_to_slots__slot(self):
        self.main_window.tab_widget.currentChanged.connect(self.on_tab_index_changed__slot)

        self.preview_images_ready_signal.connect(
            self.main_window.interface_class.detection_class.on_preview_images_ready__slot)
        self.main_window.interface_class.detection_class.image_update_needed_signal.connect(
            self.on_image_update_needed__slot)

        self.main_window.kill_threads_signal.connect(self.on_kill_threads__slot)

    def __show_detection_settings_preview(self):
        if self.detection_image_updates_needed:

            if self.settings.contains("detection_settings/preview_image_path"):
                self.__show_detection_preview_images()
            else:
                self.__show_load_image_images()

            self.detection_image_updates_needed = False

    # noinspection PyCallByClass,PyCallByClass,PyTypeChecker,PyArgumentList
    def __show_detection_preview_images(self):
        # ##### Main image preview section
        try:
            image_path = self.settings.value("detection_settings/preview_image_path", type=str)
            cv2_main_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            cv2_main_image = cv2.flip(cv2_main_image, 0)
            unaltered_cv2_copy = cv2_main_image.copy()
        except IOError:
            self.logger.error("Preview image path incorrect, or file not an image. Clearing path...")
            self.settings.remove("detection_settings/preview_image_path")
            return

        self.__draw_plate_split_line(cv2_main_image)

        self.__draw_plate_wells(cv2_main_image, True)
        self.__draw_plate_wells(cv2_main_image, False)

        self.__draw_barcode_boxes(cv2_main_image, True)
        self.__draw_barcode_boxes(cv2_main_image, False)

        self.__detect_barcode_and_show_preview(unaltered_cv2_copy, True)
        self.__detect_barcode_and_show_preview(unaltered_cv2_copy, False)

        # ##### Final touches to image, and show
        resized = cv2.resize(cv2_main_image, (UI_PREVIEW_MAIN_LB_WIDTH, UI_PREVIEW_MAIN_LB_HEIGHT))
        color_corrected = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        self.detection_main_preview_pixmap = QtGui.QPixmap.fromImage(qimage2ndarray.array2qimage(color_corrected))

        self.preview_images_ready_signal.emit()

    def __draw_plate_split_line(self, cv2_image):
        _, width, _ = cv2_image.shape
        plate_split = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", type=int)

        cv2.line(cv2_image, (0, plate_split), (width, plate_split), PLATE_SPLIT_COLOR, PLATE_LINE_THICKNESS)

    def __draw_plate_wells(self, cv2_image, is_top):
        if is_top:
            well_color = TOP_WELL_COLOR
            grid_color = TOP_WELL_GRID_COLOR

            y_offset = 0

            top_y = self.settings.value("detection_settings/alignment_and_limits/top/top_y", type=int)
            top_left_x = self.settings.value("detection_settings/alignment_and_limits/top/top_left_x", type=int)
            top_right_x = self.settings.value("detection_settings/alignment_and_limits/top/top_right_x", type=int)
            bottom_y = self.settings.value("detection_settings/alignment_and_limits/top/bottom_y", type=int)
            bottom_left_x = self.settings.value("detection_settings/alignment_and_limits/top/bottom_left_x", type=int)
            bottom_right_x = self.settings.value("detection_settings/alignment_and_limits/top/bottom_right_x", type=int)
        else:
            well_color = BOTTOM_WELL_COLOR
            grid_color = BOTTOM_WELL_GRID_COLOR

            y_offset = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", type=int)

            top_y = self.settings.value("detection_settings/alignment_and_limits/bottom/top_y", type=int)
            top_left_x = self.settings.value("detection_settings/alignment_and_limits/bottom/top_left_x", type=int)
            top_right_x = self.settings.value("detection_settings/alignment_and_limits/bottom/top_right_x", type=int)
            bottom_y = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_y", type=int)
            bottom_left_x = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_left_x",
                                                type=int)
            bottom_right_x = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_right_x",
                                                 type=int)

        # Draw bottom plate well alignment circles
        offset_per_well_x = (bottom_right_x - top_left_x) // 7
        offset_per_well_y = (bottom_y - top_y) // 11

        for x in range(PLATE_COLS):
            for y in range(PLATE_ROWS):
                if (x == 0 and y == 0) or (x == 0 and y == PLATE_ROWS) or (x == PLATE_COLS and y == 0) or (
                        x == PLATE_COLS and y == 0):
                    continue
                temp_y = (y_offset + bottom_y) - (y * offset_per_well_y)
                temp_x = top_right_x - (x * offset_per_well_x)
                cv2.circle(cv2_image, (temp_x, temp_y), WELL_CIRCLE_RADIUS, grid_color,
                           WELL_CIRCLE_THICKNESS, cv2.LINE_AA)

        cv2.circle(cv2_image, (top_left_x, top_y + y_offset), WELL_CIRCLE_RADIUS, well_color, WELL_CIRCLE_THICKNESS,
                   cv2.LINE_AA)
        cv2.circle(cv2_image, (top_right_x, top_y + y_offset), WELL_CIRCLE_RADIUS, well_color, WELL_CIRCLE_THICKNESS,
                   cv2.LINE_AA)
        cv2.circle(cv2_image, (bottom_left_x, bottom_y + y_offset), WELL_CIRCLE_RADIUS, well_color,
                   WELL_CIRCLE_THICKNESS, cv2.LINE_AA)
        cv2.circle(cv2_image, (bottom_right_x, bottom_y + y_offset), WELL_CIRCLE_RADIUS, well_color,
                   WELL_CIRCLE_THICKNESS, cv2.LINE_AA)

    def __draw_barcode_boxes(self, cv2_image, is_top):
        if is_top:
            y_offset = 0

            bc_x_size = self.settings.value("detection_settings/barcode_detection/top/barcode_x_size", type=int)
            bc_y_size = self.settings.value("detection_settings/barcode_detection/top/barcode_y_size", type=int)
            scan_x_size = self.settings.value("detection_settings/barcode_detection/top/scan_x_size", type=int)
            scan_y_size = self.settings.value("detection_settings/barcode_detection/top/scan_y_size", type=int)
            scan_x_pos = self.settings.value("detection_settings/barcode_detection/top/scan_x_position", type=int)
            scan_y_pos = self.settings.value("detection_settings/barcode_detection/top/scan_y_position", type=int)
        else:
            y_offset = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", type=int)

            bc_x_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_x_size", type=int)
            bc_y_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_y_size", type=int)
            scan_x_size = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_size", type=int)
            scan_y_size = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_size", type=int)
            scan_x_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_position", type=int)
            scan_y_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_position", type=int)

        # ##### Scan Box
        pt1_x = scan_x_pos - (scan_x_size // 2)
        pt1_y = (scan_y_pos + y_offset) - (scan_y_size // 2)

        pt2_x = scan_x_pos + (scan_x_size // 2)
        pt2_y = (scan_y_pos + y_offset) + (scan_y_size // 2)

        cv2.rectangle(cv2_image, (pt1_x, pt1_y), (pt2_x, pt2_y), SCAN_BOX_COLOR, SCAN_BOX_THICKNESS, cv2.LINE_AA)

        # ##### Barcode Box
        pt1_x = scan_x_pos - (bc_x_size // 2)
        pt1_y = (scan_y_pos + y_offset) - (bc_y_size // 2)

        pt2_x = scan_x_pos + (bc_x_size // 2)
        pt2_y = (scan_y_pos + y_offset) + (bc_y_size // 2)

        cv2.rectangle(cv2_image, (pt1_x, pt1_y), (pt2_x, pt2_y), BC_BOX_COLOR, BC_BOX_THICKNESS, cv2.LINE_AA)

    def __detect_barcode_and_show_preview(self, cv2_image, is_top):
        base_app_data_path = self.settings.value("file_transfer_and_settings/appdata_directory", type=str)
        detection_preview_bc_image_folder = base_app_data_path + "\\detection_preview_temp"

        if not exists(detection_preview_bc_image_folder):
            makedirs(detection_preview_bc_image_folder)

        code, raw, threshold = self.__try_detect_center_only(cv2_image, is_top)

        if code == "Not Found":
            code_all, raw_all, threshold_all = self.__try_detect_all(cv2_image, is_top)

            if code_all != "Not Found":
                code = code_all
                raw = raw_all
                threshold = threshold_all

        # Show the barcode
        if is_top:
            self.detection_top_bc_raw_preview_pixmap = QtGui.QPixmap.fromImage(qimage2ndarray.array2qimage(raw))
            self.detection_top_bc_threshold_preview_pixmap = QtGui.QPixmap.fromImage(
                qimage2ndarray.array2qimage(threshold))

            # Barcode number detection
            self.detection_top_bc_string = code
        else:
            self.detection_bottom_bc_raw_preview_pixmap = QtGui.QPixmap.fromImage(qimage2ndarray.array2qimage(raw))
            self.detection_bottom_bc_threshold_preview_pixmap = QtGui.QPixmap.fromImage(
                qimage2ndarray.array2qimage(threshold))

            # Barcode number detection
            self.detection_bottom_bc_string = code

    def __try_detect_center_only(self, cv2_image, is_top):
        base_app_data_path = self.settings.value("file_transfer_and_settings/appdata_directory", type=str)
        folder_path = base_app_data_path + "\\detection_preview_temp"

        if is_top:
            detection_preview_bc_image_name = "\\top.png"
            y_offset = 0

            bc_x_size = self.settings.value("detection_settings/barcode_detection/top/barcode_x_size", type=int)
            bc_y_size = self.settings.value("detection_settings/barcode_detection/top/barcode_y_size", type=int)
            scan_x_pos = self.settings.value("detection_settings/barcode_detection/top/scan_x_position", type=int)
            scan_y_pos = self.settings.value("detection_settings/barcode_detection/top/scan_y_position", type=int)

            threshold = self.settings.value("detection_settings/barcode_detection/top/threshold_center", type=int)

        else:
            detection_preview_bc_image_name = "\\bottom.png"
            y_offset = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", type=int)

            bc_x_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_x_size", type=int)
            bc_y_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_y_size", type=int)
            scan_x_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_position", type=int)
            scan_y_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_position", type=int)

            threshold = self.settings.value("detection_settings/barcode_detection/bottom/threshold_center", type=int)

        y1 = (scan_y_pos - (bc_y_size // 2)) + y_offset
        y2 = (scan_y_pos + (bc_y_size // 2)) + y_offset

        x1 = (scan_x_pos - (bc_x_size // 2))
        x2 = (scan_x_pos + (bc_x_size // 2))

        cv2_barcode_raw = cv2_image[y1:y2, x1:x2]
        cv2_barcode_gray = cv2.cvtColor(cv2_barcode_raw, cv2.COLOR_BGR2GRAY)
        ret, cv2_barcode_threshold = cv2.threshold(cv2_barcode_gray, threshold, 255, cv2.THRESH_BINARY)

        split = (folder_path + detection_preview_bc_image_name).split("\\")
        split[-1] = "original__" + split[-1]

        cv2.imwrite("\\".join(split), cv2.cvtColor(cv2_barcode_raw, cv2.COLOR_BGR2RGB))
        cv2.imwrite(folder_path + detection_preview_bc_image_name, cv2_barcode_threshold)

        resized_raw = cv2.resize(cv2_barcode_raw, (UI_PREVIEW_BC_WIDTH, UI_PREVIEW_BC_HEIGHT))
        color_corrected_raw = cv2.cvtColor(resized_raw, cv2.COLOR_BGR2RGB)

        resized_threshold = cv2.resize(cv2_barcode_threshold, (UI_PREVIEW_BC_WIDTH, UI_PREVIEW_BC_HEIGHT))
        color_corrected_threshold = cv2.cvtColor(resized_threshold, cv2.COLOR_GRAY2RGB)

        code = self.__bc_detect(folder_path + detection_preview_bc_image_name)

        if code != "Not Found":
            self.logger.info("Detection preview found plate " + str(code) + " with threshold value " + str(
                threshold) + " on \"center\" detect.")

        return code, color_corrected_raw, color_corrected_threshold

    def __try_detect_all(self, cv2_image, is_top):
        zbar_path = self.settings.value("file_and_transfer_settings/zbar_path", type=str)
        base_app_data_path = self.settings.value("file_transfer_and_settings/appdata_directory", type=str)
        detection_preview_bc_image_folder = base_app_data_path + "\\detection_preview_temp"

        if is_top:
            y_offset = 0

            bc_x_size = self.settings.value("detection_settings/barcode_detection/top/barcode_x_size", type=int)
            bc_y_size = self.settings.value("detection_settings/barcode_detection/top/barcode_y_size", type=int)
            scan_x_size = self.settings.value("detection_settings/barcode_detection/top/scan_x_size", type=int)
            scan_y_size = self.settings.value("detection_settings/barcode_detection/top/scan_y_size", type=int)
            scan_x_pos = self.settings.value("detection_settings/barcode_detection/top/scan_x_position", type=int)
            scan_y_pos = self.settings.value("detection_settings/barcode_detection/top/scan_y_position", type=int)

            threshold_center = self.settings.value("detection_settings/barcode_detection/top/threshold_center",
                                                   type=int)
            threshold_range = self.settings.value("detection_settings/barcode_detection/top/threshold_range", type=int)

        else:
            y_offset = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", type=int)

            bc_x_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_x_size", type=int)
            bc_y_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_y_size", type=int)
            scan_x_size = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_size", type=int)
            scan_y_size = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_size", type=int)
            scan_x_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_position", type=int)
            scan_y_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_position", type=int)

            threshold_center = self.settings.value("detection_settings/barcode_detection/bottom/threshold_center",
                                                   type=int)
            threshold_range = self.settings.value("detection_settings/barcode_detection/bottom/threshold_range",
                                                  type=int)

        y_bound_upper = (scan_y_pos - (scan_y_size // 2)) + y_offset
        x_bound_left = (scan_x_pos - (scan_x_size // 2))

        num_x_increments = (scan_x_size - bc_x_size) // DETECT_ALL_X_INCREMENT
        num_y_increments = (scan_y_size - bc_y_size) // DETECT_ALL_Y_INCREMENT
        num_thresh_increments = (threshold_range * 2) + 1
        threshold_min = threshold_center - threshold_range

        workers = []

        self.barcode_found = False

        for y in range(num_y_increments):
            for x in range(num_x_increments):
                for thr in range(num_thresh_increments):
                    if not self.barcode_found:
                        y1 = y_bound_upper + (y * DETECT_ALL_Y_INCREMENT)
                        y2 = y1 + bc_y_size
                        x1 = x_bound_left + (x * DETECT_ALL_X_INCREMENT)
                        x2 = x1 + bc_x_size

                        current_threshold = threshold_min + thr

                        worker = WorkerCore.DetectionWorker(self, y1, y2, x1, x2, current_threshold, cv2_image,
                                                            detection_preview_bc_image_folder, zbar_path)
                        workers.append(worker)

        for worker in workers:
            worker.wait()
            result = worker.result
            threshold_value = str(worker.threshold)
            raw_cv2 = worker.cv2_raw
            threshold_cv2 = worker.cv2_threshold

            if result != "Not Found":
                if result == "No Plate Present":
                    self.logger.info("Detection preview found could not detect a plate.")
                else:
                    self.logger.info(
                        "Detection preview found plate " + result + " with threshold value " + threshold_value + " on \"full\" detect.")
                    return result, raw_cv2, threshold_cv2

                break

        return "Not Found", 0, 0

    def __bc_detect(self, threshold_image_path):
        zbar_path = self.settings.value("file_and_transfer_settings/zbar_path", type=str)

        if zbar_path:
            process = subprocess.Popen([zbar_path, "--raw", "-q", threshold_image_path], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            out, err = process.communicate()
            out = out.decode("utf-8").strip('\n')

            if out != "":
                return out

        return "Not Found"

    # noinspection PyCallByClass,PyCallByClass,PyTypeChecker,PyArgumentList
    def __show_load_image_images(self):
        self.detection_main_preview_pixmap = QtGui.QPixmap(UI_PREVIEW_LOAD_IMAGE_MAIN_PATH)

        bc_pixmap_temp = QtGui.QPixmap(UI_PREVIEW_LOAD_IMAGE_BC_PATH)
        self.detection_top_bc_raw_preview_pixmap = bc_pixmap_temp
        self.detection_top_bc_threshold_preview_pixmap = bc_pixmap_temp
        self.detection_bottom_bc_raw_preview_pixmap = bc_pixmap_temp
        self.detection_bottom_bc_threshold_preview_pixmap = bc_pixmap_temp

        self.preview_images_ready_signal.emit()

    def on_barcode_found__slot(self):
        self.barcode_found = True

    def on_tab_index_changed__slot(self, index):
        if index == 1:
            self.detection_settings_tab_open = True
        else:
            self.detection_settings_tab_open = False

    def on_image_update_needed__slot(self):
        self.detection_image_updates_needed = True

    def on_kill_threads__slot(self):
        self.run_thread_flag = False
