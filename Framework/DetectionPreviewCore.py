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
# from PIL import Image, PngImagePlugin, ImageQt
import cv2
import qimage2ndarray

# Settings for imports
# Image.MAX_IMAGE_PIXELS = None  # This disables the decompression bomb warning

#####################################
# Global Variables
#####################################
UI_PREVIEW_LOAD_IMAGE_MAIN_PATH = "Resources/UI/preview_please_load_image_main.png"
UI_PREVIEW_LOAD_IMAGE_BC_PATH = "Resources/UI/preview_please_load_image_barcode.png"

UI_PREVIEW_MAIN_LB_WIDTH = 280
UI_PREVIEW_MAIN_LB_HEIGHT = 830

PLATE_ROWS = 12
PLATE_COLS = 8

PLATE_SPLIT_COLOR = (0, 0, 255)  # BGR -> Full Red
PLATE_LINE_THICKNESS = 150

TOP_WELL_COLOR = (32, 50, 1)  # BGR -> Dark Green
TOP_WELL_GRID_COLOR = (0, 255, 0)  # BGR -> Full Green
BOTTOM_WELL_COLOR = (128, 0, 0)  # BGR -> Navy Blue
BOTTOM_WELL_GRID_COLOR = (255, 0, 0)  # BGR -> Full Green
WELL_CIRCLE_THICKNESS = 100
WELL_CIRCLE_RADIUS = 360


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
        self.detection_bottom_bc_raw_preview_pixmap = None
        self.detection_bottom_bc_threshold_preview_pixmap = None

        self.detection_image_updates_needed = True

        # ########## Load class settings ##########
        self.__load_settings()

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

        # ########## Start Thread ##########
        self.start()

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
    def __connect_signals_to_slots(self):
        self.main_window.tab_widget.currentChanged.connect(self.on_tab_index_changed__slot)

        self.preview_images_ready_signal.connect(self.main_window.interface_class.detection_class.on_preview_images_ready__slot)
        self.main_window.interface_class.detection_class.image_update_needed_signal.connect(self.on_image_update_needed__slot)

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
        except IOError:
            self.logger.error("Preview image path incorrect, or file not an image. Clearing path...")
            self.settings.remove("detection_settings/preview_image_path")
            return

        # Settings and variables for drawing
        height, width, channels = cv2_main_image.shape
        plate_split = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", type=int)
        top_bottom_y = self.settings.value("detection_settings/alignment_and_limits/top/bottom_y", type=int)
        top_left_x = self.settings.value("detection_settings/alignment_and_limits/top/left_x", type=int)
        top_right_x = self.settings.value("detection_settings/alignment_and_limits/top/right_x", type=int)
        bottom_bottom_y = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_y", type=int)
        bottom_left_x = self.settings.value("detection_settings/alignment_and_limits/bottom/left_x", type=int)
        bottom_right_x = self.settings.value("detection_settings/alignment_and_limits/bottom/right_x", type=int)

        # Draw plate split line
        cv2.line(cv2_main_image, (0, plate_split), (width, plate_split), PLATE_SPLIT_COLOR, PLATE_LINE_THICKNESS)

        # Draw top plate well alignment circles
        offset_per_well = (top_right_x - top_left_x) // 7

        for x in range(PLATE_COLS):
            for y in range(PLATE_ROWS):
                temp_y = top_bottom_y - (y * offset_per_well)
                temp_x = top_right_x - (x * offset_per_well)
                cv2.circle(cv2_main_image, (temp_x, temp_y), WELL_CIRCLE_RADIUS, TOP_WELL_GRID_COLOR, WELL_CIRCLE_THICKNESS, cv2.LINE_AA)

        cv2.circle(cv2_main_image, (top_left_x, top_bottom_y), WELL_CIRCLE_RADIUS, TOP_WELL_COLOR, WELL_CIRCLE_THICKNESS, cv2.LINE_AA)
        cv2.circle(cv2_main_image, (top_right_x, top_bottom_y), WELL_CIRCLE_RADIUS, TOP_WELL_COLOR, WELL_CIRCLE_THICKNESS, cv2.LINE_AA)

        # Draw bottom plate well alignment circles
        cv2.circle(cv2_main_image, (bottom_left_x, bottom_bottom_y), WELL_CIRCLE_RADIUS, BOTTOM_WELL_COLOR, WELL_CIRCLE_THICKNESS, cv2.LINE_AA)
        cv2.circle(cv2_main_image, (bottom_right_x, bottom_bottom_y), WELL_CIRCLE_RADIUS, BOTTOM_WELL_COLOR, WELL_CIRCLE_THICKNESS, cv2.LINE_AA)

        resized = cv2.resize(cv2_main_image, (UI_PREVIEW_MAIN_LB_WIDTH, UI_PREVIEW_MAIN_LB_HEIGHT))
        color_corrected = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        self.detection_main_preview_pixmap = QtGui.QPixmap.fromImage(qimage2ndarray.array2qimage(color_corrected))

        # ##### Barcode preview section

        self.preview_images_ready_signal.emit()

    # noinspection PyCallByClass,PyCallByClass,PyTypeChecker,PyArgumentList
    def __show_load_image_images(self):
        self.detection_main_preview_pixmap = QtGui.QPixmap(UI_PREVIEW_LOAD_IMAGE_MAIN_PATH)

        bc_pixmap_temp = QtGui.QPixmap(UI_PREVIEW_LOAD_IMAGE_BC_PATH)
        self.detection_top_bc_raw_preview_pixmap = bc_pixmap_temp
        self.detection_top_bc_threshold_preview_pixmap = bc_pixmap_temp
        self.detection_bottom_bc_raw_preview_pixmap = bc_pixmap_temp
        self.detection_bottom_bc_threshold_preview_pixmap = bc_pixmap_temp

        self.preview_images_ready_signal.emit()

    def on_tab_index_changed__slot(self, index):
        if index == 1:
            self.detection_settings_tab_open = True
        else:
            self.detection_settings_tab_open = False

    def on_image_update_needed__slot(self):
        self.detection_image_updates_needed = True

    def on_kill_threads__slot(self):
        self.run_thread_flag = False


