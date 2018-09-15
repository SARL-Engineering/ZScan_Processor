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
from PIL import Image, ImageQt

# Custom imports
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI

#####################################
# Global Variables
#####################################
Image.MAX_IMAGE_PIXELS = None  # Disables decompression bomb assertion


#####################################
# PreviewProcessor Definition
#####################################
class PreviewProcessor(QtCore.QThread):

    def __init__(self, shared_objects):
        super(PreviewProcessor, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## References to GUI Elements ##########
        self.main_tab_widget = self.main_screen.main_tab_widget  # type: QtWidgets.QTabWidget
        self.settings_tab_widget = self.main_screen.settings_tab_widget  # type: QtWidgets.QTabWidget

        self.preview_image_path_line_edit = self.main_screen.preview_image_path_line_edit  # QtWidgets.QLineEdit

        self.plate_spliting_image_label = self.main_screen.plate_spliting_image_label  # QtWidgets.QLabel

        self.top_plate_image_label = self.main_screen.top_plate_image_label  # QtWidgets.QLabel
        self.top_plate_original_image_label = self.main_screen.top_plate_original_image_label  # QtWidgets.QLabel
        self.top_plate_threshold_image_label = self.main_screen.top_plate_threshold_image_label  # QtWidgets.QLabel
        self.top_plate_barcode_value_label = self.main_screen.top_plate_barcode_value_label  # QtWidgets.QLabel

        self.bottom_plate_image_label = self.main_screen.bottom_plate_image_label  # QtWidgets.QLabel
        self.bottom_plate_original_image_label = self.main_screen.bottom_plate_original_image_label  # QtWidgets.QLabel
        self.bottom_plate_threshold_image_label = self.main_screen.bottom_plate_threshold_image_label  # QtWidgets.QLabel
        self.bottom_plate_barcode_value_label = self.main_screen.bottom_plate_barcode_value_label  # QtWidgets.QLabel

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########
        self.preview_image_path_changed = False
        self.attempted_preview_image_load = False

        self.preview_image = None  # type: Image

        # ########## Setup program start signal connections ##########
        self.setup_signals()

    def run(self):
        self.logger.debug("Preview Processor Thread Starting...")

        while self.run_thread_flag:
            self.process_previews()
            self.msleep(10)

        self.logger.debug("Preview Processor Thread Stopping...")

    def process_previews(self):
        self.check_if_preview_image_valid_and_load()

        main_tab_on_settings = self.main_tab_widget.currentWidget().objectName() == "settings_tab"

        if self.preview_image and main_tab_on_settings:
            current_settings_tab = self.settings_tab_widget.currentWidget().objectName()

            if current_settings_tab == "settings_plate_splitting_tab":
                self.show_plate_splitting_preview()
            elif current_settings_tab == "settings_top_plate_tab":
                self.show_top_plate_preview()
            elif current_settings_tab == "settings_bottom_plate_tab":
                self.show_bottom_plate_preview()

    def check_if_preview_image_valid_and_load(self):
        if (not self.preview_image or self.preview_image_path_changed) and not self.attempted_preview_image_load:
            try:
                self.preview_image = Image.open(self.preview_image_path_line_edit.text())
                self.logger.debug("Preview image loaded successfully!")
            except IOError:
                self.attempted_preview_image_load = True
                self.preview_image = None
                self.logger.warning("Preview image is invalid. Please choose another image...")
            except Exception as e:
                self.logger.error(e)
                raise e

            self.preview_image_path_changed = False

    def show_plate_splitting_preview(self):
        pass

    def show_top_plate_preview(self):
        pass

    def show_bottom_plate_preview(self):
        pass

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        self.preview_image_path_line_edit.textChanged.connect(self.on_preview_image_path_changed__slot)

    def on_preview_image_path_changed__slot(self):
        self.attempted_preview_image_load = False
        self.preview_image_path_changed = True

    def on_kill_threads__slot(self):
        self.run_thread_flag = False

    def setup_signals(self):
        self.core_signals["start"].connect(self.start)
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)