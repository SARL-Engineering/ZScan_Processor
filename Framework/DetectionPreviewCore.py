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
from PIL import Image, PngImagePlugin, ImageQt

# Settings for imports
Image.MAX_IMAGE_PIXELS = None  # This disables the decompression bomb warning

#####################################
# Global Variables
#####################################
UI_PREVIEW_LOAD_IMAGE_MAIN_PATH = "Resources/UI/preview_please_load_image_main.png"
UI_PREVIEW_LOAD_IMAGE_BC_PATH = "Resources/UI/preview_please_load_image_barcode.png"

UI_PREVIEW_MAIN_LB_WIDTH = 280
UI_PREVIEW_MAIN_LB_HEIGHT = 830


#####################################
# Detection Preview Class Definition
#####################################
class DetectionPreview(QtCore.QThread):

    preview_main_image_ready_signal = QtCore.pyqtSignal()

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
        self.detection_image_displayed = False

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

        self.preview_main_image_ready_signal.connect(self.main_window.interface_class.detection_class.on_main_preview_image_ready__slot)
        self.main_window.interface_class.detection_class.detection_preview_image_displayed_signal.connect(self.on_detection_preview_image_displayed__slot)

        self.main_window.kill_threads_signal.connect(self.on_kill_threads__slot)

    # noinspection PyCallByClass,PyCallByClass,PyTypeChecker,PyArgumentList
    def __show_detection_settings_preview(self):

        if self.settings.contains("detection_settings/preview_image_path"):
            main_preview_pil_image = None

            try:
                image_path = self.settings.value("detection_settings/preview_image_path", type=str)
                main_preview_pil_image = Image.open(image_path)
            except IOError:
                self.logger.error("Preview image path incorrect, or file not an image. Clearing path...")
                self.settings.remove("detection_settings/preview_image_path")
                return

            resized = main_preview_pil_image.resize((UI_PREVIEW_MAIN_LB_WIDTH, UI_PREVIEW_MAIN_LB_HEIGHT))
            self.detection_main_preview_pixmap = QtGui.QPixmap.fromImage(ImageQt.ImageQt(resized))
            self.detection_main_preview_pixmap.detach()
            self.detection_image_displayed = False
            self.preview_main_image_ready_signal.emit()

            while not self.detection_image_displayed:
                self.msleep(100)

        else:
            temp_img = Image.open(UI_PREVIEW_LOAD_IMAGE_MAIN_PATH)  # type: PngImagePlugin.PngImageFile
            resized = temp_img.resize((UI_PREVIEW_MAIN_LB_WIDTH, UI_PREVIEW_MAIN_LB_HEIGHT))
            self.detection_main_preview_pixmap = QtGui.QPixmap.fromImage(ImageQt.ImageQt(resized))
            self.detection_main_preview_pixmap.detach()
            self.detection_image_displayed = False
            self.preview_main_image_ready_signal.emit()

            while not self.detection_image_displayed:
                self.msleep(100)

        # main_preview_pil_image = Image.open("C:/Users/Corwin Perren/Pictures/Scanner Barcode Testing/000010186004.tif")  # type: Image
        # main_preview_pil_image = main_preview_pil_image.transpose(Image.FLIP_LEFT_RIGHT)
        # main_preview_pil_image = main_preview_pil_image.rotate(180)
        # print("Image type: " + str(main_preview_pil_image.mode))
        # print(ImageQt.ImageQt(main_preview_pil_image))

        self.msleep(500)

    def on_tab_index_changed__slot(self, index):
        if index == 1:
            self.detection_settings_tab_open = True
        else:
            self.detection_settings_tab_open = False

    def on_detection_preview_image_displayed__slot(self):
        self.detection_image_displayed = True

    def on_kill_threads__slot(self):
        self.run_thread_flag = False


