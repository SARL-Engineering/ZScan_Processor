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
import qimage2ndarray
import numpy as np

# Custom imports
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI
from Resources import Constants


#####################################
# Global Variables
#####################################


#####################################
# PreviewProcessor Definition
#####################################
class PreviewProcessor(QtCore.QThread):
    request_image_update__signal = QtCore.pyqtSignal()

    black_image = np.zeros((1000, 1000, 3), np.uint8)

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

        self.preview_image = None

        self.plate_split_image_pixmap = None
        self.output_pixmap_groups = None

        self.image_mappings = {
            "settings_plate_splitting_tab": {
                "plate_split_main_preview": {
                    "size": (1460, 494),
                    "element": self.plate_spliting_image_label
                }
            },

            "settings_top_plate_tab": {
                "top_main_preview": {
                    "size": (702, 475),
                    "element": self.top_plate_image_label
                },

                "top_original_barcode_preview": {
                    "size": (450, 45),
                    "element": self.top_plate_original_image_label
                },

                "top_threshold_barcode_preview": {
                    "size": (450, 45),
                    "element": self.top_plate_threshold_image_label
                }
            },

            "settings_bottom_plate_tab": {
                "bottom_main_preview": {
                    "size": (702, 475),
                    "element": self.bottom_plate_image_label
                },

                "bottom_original_barcode_preview": {
                    "size": (450, 45),
                    "element": self.bottom_plate_original_image_label
                },

                "bottom_threshold_barcode_preview": {
                    "size": (450, 45),
                    "element": self.bottom_plate_threshold_image_label
                }
            }
        }

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

        if self.preview_image is not None and main_tab_on_settings:
            current_settings_tab = self.settings_tab_widget.currentWidget().objectName()

            if current_settings_tab == "settings_plate_splitting_tab":
                self.show_plate_splitting_preview()
            elif current_settings_tab == "settings_top_plate_tab":
                self.show_top_plate_preview()
            elif current_settings_tab == "settings_bottom_plate_tab":
                self.show_bottom_plate_preview()

    def check_if_preview_image_valid_and_load(self):
        self.reset_and_show_black_preview_images_if_needed()

        if (self.preview_image is None or self.preview_image_path_changed) and not self.attempted_preview_image_load:
            try:
                if self.preview_image_path_line_edit.text() != "*** No Path Set ***":
                    self.preview_image = cv2.imread(self.preview_image_path_line_edit.text())

                    if self.preview_image is None:
                        raise IOError

                    self.preview_image = cv2.rotate(self.preview_image, 0)
                    self.preview_image = cv2.flip(self.preview_image, 0)

                    self.logger.debug("Preview image loaded successfully!")
                self.attempted_preview_image_load = True
            except IOError or cv2.error:
                self.logger.warning("Preview image is invalid. Please choose another image...")
                self.attempted_preview_image_load = True
                self.preview_image = None
            except Exception as e:
                self.logger.error(e)

            self.preview_image_path_changed = False

    def reset_and_show_black_preview_images_if_needed(self):
        if self.preview_image_path_changed:
            output_image_group = []

            for tab in self.image_mappings.keys():
                for element in self.image_mappings[tab]:
                    output_image_group.append((self.black_image, self.image_mappings[tab][element]))

            self.set_pixmap_from_image_groups_and_show(output_image_group)

    def show_plate_splitting_preview(self):
        plate_split_line_location = self.settings.value("gui_elements/alignment_shared_split_line_spinbox", type=int)
        split_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_split"]["color"]
        split_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_split"]["thickness"]

        plate_split_preview = self.preview_image.copy()
        height, _, _ = plate_split_preview.shape

        cv2.line(plate_split_preview, (plate_split_line_location, 0), (plate_split_line_location, height), split_color,
                 split_thickness)

        output_image_group = [
            (plate_split_preview, self.image_mappings["settings_plate_splitting_tab"]["plate_split_main_preview"])
        ]

        self.set_pixmap_from_image_groups_and_show(output_image_group)

    def show_top_plate_preview(self):
        plate_split_line_location = self.settings.value("gui_elements/alignment_shared_split_line_spinbox", type=int)

        a1_x_location = self.settings.value("gui_elements/top_a1_x_spinbox", type=int)
        a1_y_location = self.settings.value("gui_elements/top_a1_y_spinbox", type=int)
        h12_x_location = self.settings.value("gui_elements/top_h12_x_spinbox", type=int)
        h12_y_location = self.settings.value("gui_elements/top_h12_y_spinbox", type=int)

        well_radius = self.settings.value("gui_elements/top_well_radius_spinbox", type=int)
        well_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["color"]
        well_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["thickness"]
        well_marker_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_marker_wells"]["color"]
        well_marker_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_marker_wells"]["thickness"]

        num_rows = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["rows"]
        num_columns = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["columns"]

        top_plate_preview = self.preview_image.copy()
        height, width, _ = top_plate_preview.shape

        top_plate_preview = top_plate_preview[0:height, 0:plate_split_line_location]

        # ##### CIRCLES #####
        offset_per_well_x = (h12_x_location - a1_x_location) / (num_columns - 1)
        offset_per_well_y = (h12_y_location - a1_y_location) / (num_rows - 1)

        locations = []

        for x in range(num_columns):
            for y in range(num_rows):
                locations.append((int(a1_x_location + (x * offset_per_well_x)), int(a1_y_location + (y * offset_per_well_y))))

        locations = set(locations)

        try:
            locations.remove((a1_x_location, a1_y_location))
            locations.remove((h12_x_location, h12_y_location))
        except Exception as _:
            self.logger.debug("Could not remove marker wells. ")

        for location in locations:
            cv2.circle(top_plate_preview, location, well_radius, well_color, well_thickness, cv2.LINE_AA)

        cv2.circle(top_plate_preview, (a1_x_location, a1_y_location), well_radius, well_marker_color,
                   well_marker_thickness, cv2.LINE_AA)
        cv2.circle(top_plate_preview, (h12_x_location, h12_y_location), well_radius, well_marker_color,
                   well_marker_thickness, cv2.LINE_AA)

        # ###################

        output_image_group = [
            (top_plate_preview, self.image_mappings["settings_top_plate_tab"]["top_main_preview"])
        ]

        self.set_pixmap_from_image_groups_and_show(output_image_group)

    def show_bottom_plate_preview(self):
        plate_split_line_location = self.settings.value("gui_elements/alignment_shared_split_line_spinbox", type=int)

        a1_x_location = self.settings.value("gui_elements/bottom_a1_x_spinbox", type=int)
        a1_y_location = self.settings.value("gui_elements/bottom_a1_y_spinbox", type=int)
        h12_x_location = self.settings.value("gui_elements/bottom_h12_x_spinbox", type=int)
        h12_y_location = self.settings.value("gui_elements/bottom_h12_y_spinbox", type=int)

        well_radius = self.settings.value("gui_elements/bottom_well_radius_spinbox", type=int)
        well_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["color"]
        well_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["thickness"]
        well_marker_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_marker_wells"]["color"]
        well_marker_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_marker_wells"]["thickness"]

        num_rows = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["rows"]
        num_columns = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["columns"]

        bottom_plate_preview = self.preview_image.copy()
        height, width, _ = bottom_plate_preview.shape

        bottom_plate_preview = bottom_plate_preview[0:height, plate_split_line_location:width]

        # ##### CIRCLES #####
        offset_per_well_x = (h12_x_location - a1_x_location) / (num_columns - 1)
        offset_per_well_y = (h12_y_location - a1_y_location) / (num_rows - 1)

        locations = []

        for x in range(num_columns):
            for y in range(num_rows):
                locations.append(
                    (int(a1_x_location + (x * offset_per_well_x)), int(a1_y_location + (y * offset_per_well_y))))

        locations = set(locations)

        try:
            locations.remove((a1_x_location, a1_y_location))
            locations.remove((h12_x_location, h12_y_location))
        except Exception as _:
            self.logger.debug("Could not remove marker wells. ")

        for location in locations:
            cv2.circle(bottom_plate_preview, location, well_radius, well_color, well_thickness, cv2.LINE_AA)

        cv2.circle(bottom_plate_preview, (a1_x_location, a1_y_location), well_radius, well_marker_color,
                   well_marker_thickness, cv2.LINE_AA)
        cv2.circle(bottom_plate_preview, (h12_x_location, h12_y_location), well_radius, well_marker_color,
                   well_marker_thickness, cv2.LINE_AA)

        # ###################

        output_image_group = [
            (bottom_plate_preview, self.image_mappings["settings_bottom_plate_tab"]["bottom_main_preview"])
        ]

        self.set_pixmap_from_image_groups_and_show(output_image_group)

    def set_pixmap_from_image_groups_and_show(self, output_image_group):
        self.output_pixmap_groups = []

        for image_group in output_image_group:
            resized_pixmap = QtGui.QPixmap.fromImage(
                qimage2ndarray.array2qimage(cv2.resize(image_group[0], image_group[1]["size"])))
            self.output_pixmap_groups.append((resized_pixmap, image_group[1]["element"]))

        self.request_image_update__signal.emit()

    def on_preview_image_path_changed__slot(self):
        self.attempted_preview_image_load = False
        self.preview_image_path_changed = True

    def on_image_update_requested__slot(self):
        for pixmap_group in self.output_pixmap_groups:
            try:
                pixmap_group[1].setPixmap(pixmap_group[0])
            except Exception as e:
                print(e)

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        self.preview_image_path_line_edit.textChanged.connect(self.on_preview_image_path_changed__slot)

        self.request_image_update__signal.connect(self.on_image_update_requested__slot)

    def on_kill_threads__slot(self):
        self.run_thread_flag = False

    def setup_signals(self):
        self.core_signals["start"].connect(self.start)
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)
