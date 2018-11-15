#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging
import cv2
from PIL import ImageFont, ImageDraw, Image
import qimage2ndarray
import numpy as np
from os.path import getsize
from time import time

# Custom imports
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI
from Resources import Constants

from Framework.DetectionProcessing import DetectionProcessorCore
from Framework import ImageProcessing

#####################################
# Global Variables
#####################################
NO_PATH_SET_STRING = "*** No Path Set ***"
NO_PATH_NA_STRING = "N/A"

NO_BARCODE_NA_STRING = "N/A"

SIZE_DIVISOR = 1024000

PREVIEW_EXAMPLE_TEXT = "000000000"

WELL_PREVIEW_BOX_SCALAR = 1.2

WELLS_ADJUST_RESET_TIMEOUT = 5  # Seconds


#####################################
# PreviewProcessor Definition
#####################################
class PreviewProcessor(QtCore.QThread):
    request_image_update__signal = QtCore.pyqtSignal()
    top_barcode_text_update_ready__signal = QtCore.pyqtSignal(str)
    bottom_barcode_text_update_ready__signal = QtCore.pyqtSignal(str)

    progress_bar_status_update_requested__signal = QtCore.pyqtSignal(int)

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

        self.preview_image_path_line_edit = self.main_screen.preview_image_path_line_edit  # type: QtWidgets.QLineEdit
        self.preview_image_x_size_label = self.main_screen.preview_image_x_size_label  # type: QtWidgets.QLabel
        self.preview_image_y_size_label = self.main_screen.preview_image_y_size_label  # type: QtWidgets.QLabel
        self.preview_image_file_size_label = self.main_screen.preview_image_file_size_label  # type: QtWidgets.QLabel

        self.plate_spliting_image_label = self.main_screen.plate_spliting_image_label  # type: QtWidgets.QLabel

        self.top_plate_image_label = self.main_screen.top_plate_image_label  # type: QtWidgets.QLabel
        self.top_plate_original_image_label = self.main_screen.top_plate_original_image_label  # type: QtWidgets.QLabel
        self.top_plate_threshold_image_label = \
            self.main_screen.top_plate_threshold_image_label  # type: QtWidgets.QLabel
        self.top_plate_barcode_value_label = self.main_screen.top_plate_barcode_value_label  # type: QtWidgets.QLabel
        self.top_plate_well_preview_image_label = \
            self.main_screen.top_plate_well_preview_image_label  # type: QtWidgets.QLabel

        self.bottom_plate_image_label = self.main_screen.bottom_plate_image_label  # type: QtWidgets.QLabel
        self.bottom_plate_original_image_label = \
            self.main_screen.bottom_plate_original_image_label  # type: QtWidgets.QLabel
        self.bottom_plate_threshold_image_label = \
            self.main_screen.bottom_plate_threshold_image_label  # type: QtWidgets.QLabel
        self.bottom_plate_barcode_value_label = \
            self.main_screen.bottom_plate_barcode_value_label  # type: QtWidgets.QLabel
        self.bottom_plate_well_preview_image_label = \
            self.main_screen.bottom_plate_well_preview_image_label  # type: QtWidgets.QLabel

        self.top_well_min_radius_spinbox = self.main_screen.top_well_min_radius_spinbox  # type:QtWidgets.QSpinBox
        self.top_well_max_radius_spinbox = self.main_screen.top_well_max_radius_spinbox  # type:QtWidgets.QSpinBox
        self.top_well_min_between_spinbox = self.main_screen.top_well_min_between_spinbox  # type:QtWidgets.QSpinBox
        self.top_well_detection_blur_spinbox = self.main_screen.top_well_detection_blur_spinbox  # type:QtWidgets.QSpinBox
        self.top_well_detection_threshold_1_spinbox = self.main_screen.top_well_detection_threshold_1_spinbox  # type:QtWidgets.QSpinBox
        self.top_well_detection_threshold_2_spinbox = self.main_screen.top_well_detection_threshold_2_spinbox  # type:QtWidgets.QSpinBox

        self.bottom_well_min_radius_spinbox = self.main_screen.bottom_well_min_radius_spinbox  # type:QtWidgets.QSpinBox
        self.bottom_well_max_radius_spinbox = self.main_screen.bottom_well_max_radius_spinbox  # type:QtWidgets.QSpinBox
        self.bottom_well_min_between_spinbox = self.main_screen.bottom_well_min_between_spinbox  # type:QtWidgets.QSpinBox
        self.bottom_well_detection_blur_spinbox = self.main_screen.bottom_well_detection_blur_spinbox  # type:QtWidgets.QSpinBox
        self.bottom_well_detection_threshold_1_spinbox = self.main_screen.bottom_well_detection_threshold_1_spinbox  # type:QtWidgets.QSpinBox
        self.bottom_well_detection_threshold_2_spinbox = self.main_screen.bottom_well_detection_threshold_2_spinbox  # type:QtWidgets.QSpinBox

        self.processing_progress_bar = self.main_screen.processing_progress_bar  # type: QtWidgets.QProgressBar

        self.continuous_detection_checkbox = self.main_screen.continuous_detection_checkbox  # type: QtWidgets.QCheckBox
        self.single_detection_button = self.main_screen.single_detection_button  # type: QtWidgets.QPushButton

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########
        self.preview_image_path_changed = False
        self.attempted_preview_image_load = False

        self.detect_once = False
        self.detect_continuous = False

        self.top_wells = None
        self.bottom_wells = None

        self.top_wells_reset_last_time = None
        self.bottom_wells_reset_last_time = None

        self.preview_image = None
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
                },

                "top_well_preview": {
                    "size": (300, 300),
                    "element": self.top_plate_well_preview_image_label
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
                },

                "bottom_well_preview": {
                    "size": (300, 300),
                    "element": self.bottom_plate_well_preview_image_label
                }
            }
        }

        # ########## Setup program start signal connections ##########
        self.setup_signals()

    def run(self):
        self.logger.debug("Preview Processor Thread Starting...")

        while self.run_thread_flag:
            self.process_previews()
            self.process_detection_if_needed()
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

    def process_detection_if_needed(self):
        self.reset_barcode_detect_images_if_needed()

        if self.detect_once or self.detect_continuous:
            self.progress_bar_status_update_requested__signal.emit(0)

            main_tab_on_settings = self.main_tab_widget.currentWidget().objectName() == "settings_tab"

            if self.preview_image is not None and main_tab_on_settings:
                current_settings_tab = self.settings_tab_widget.currentWidget().objectName()

                if current_settings_tab == "settings_top_plate_tab":
                    self.detect_top()
                elif current_settings_tab == "settings_bottom_plate_tab":
                    self.detect_bottom()

            self.progress_bar_status_update_requested__signal.emit(1)
            self.detect_once = False

    def check_if_preview_image_valid_and_load(self):
        self.reset_and_show_black_preview_images_if_needed()
        self.reset_file_information_if_needed()
        self.reset_wells_detection_if_needed()

        if (self.preview_image is None or self.preview_image_path_changed) and not self.attempted_preview_image_load:
            self.progress_bar_status_update_requested__signal.emit(0)

            preview_image_path = self.preview_image_path_line_edit.text()
            try:
                if preview_image_path != NO_PATH_SET_STRING:
                    self.preview_image = cv2.imread(preview_image_path)

                    if self.preview_image is None:
                        raise IOError

                    self.preview_image = cv2.cvtColor(self.preview_image, cv2.COLOR_BGR2RGB)
                    self.preview_image = cv2.rotate(self.preview_image, 0)
                    self.preview_image = cv2.flip(self.preview_image, 0)

                    height, width, _ = self.preview_image.shape

                    self.preview_image_x_size_label.setText("%d px" % width)
                    self.preview_image_y_size_label.setText("%d px" % height)
                    self.preview_image_file_size_label.setText("%d MB" % (getsize(preview_image_path) // SIZE_DIVISOR))

                    self.logger.debug("Preview image loaded successfully!")
                self.attempted_preview_image_load = True
            except IOError or cv2.error:
                self.logger.warning("Preview image is invalid. Please choose another image...")
                self.preview_image_path_line_edit.setText(NO_PATH_SET_STRING)
                self.attempted_preview_image_load = True
                self.preview_image = None
            except Exception as e:
                self.logger.error(e)

            self.progress_bar_status_update_requested__signal.emit(1)
            self.preview_image_path_changed = False

    def reset_barcode_detect_images_if_needed(self):
        if self.detect_once:
            output_image_group = [
                (self.black_image,
                 self.image_mappings["settings_bottom_plate_tab"]["bottom_original_barcode_preview"]),
                (self.black_image,
                 self.image_mappings["settings_bottom_plate_tab"]["bottom_threshold_barcode_preview"]),
                (self.black_image,
                 self.image_mappings["settings_top_plate_tab"]["top_original_barcode_preview"]),
                (self.black_image,
                 self.image_mappings["settings_top_plate_tab"]["top_threshold_barcode_preview"]),
            ]

            self.top_barcode_text_update_ready__signal.emit(NO_BARCODE_NA_STRING)
            self.bottom_barcode_text_update_ready__signal.emit(NO_BARCODE_NA_STRING)

            self.set_pixmap_from_image_groups_and_show(output_image_group)

    def reset_and_show_black_preview_images_if_needed(self):
        if self.preview_image_path_changed:
            output_image_group = []

            for tab in self.image_mappings.keys():
                for element in self.image_mappings[tab]:
                    output_image_group.append((self.black_image, self.image_mappings[tab][element]))

            self.top_barcode_text_update_ready__signal.emit(NO_BARCODE_NA_STRING)
            self.bottom_barcode_text_update_ready__signal.emit(NO_BARCODE_NA_STRING)

            self.set_pixmap_from_image_groups_and_show(output_image_group)

    def reset_file_information_if_needed(self):
        if self.preview_image_path_changed:
            self.preview_image_x_size_label.setText(NO_PATH_NA_STRING)
            self.preview_image_y_size_label.setText(NO_PATH_NA_STRING)
            self.preview_image_file_size_label.setText(NO_PATH_NA_STRING)

            self.top_wells = None
            self.bottom_wells = None

    def reset_wells_detection_if_needed(self):
        should_reset_top = False
        should_reset_bottom = False

        if self.preview_image_path_changed:
            should_reset_top = True
            should_reset_bottom = True

        if self.top_wells_reset_last_time is not None:
            time_diff = time() - self.top_wells_reset_last_time

            if time_diff > WELLS_ADJUST_RESET_TIMEOUT:
                should_reset_top = True

        if self.bottom_wells_reset_last_time is not None:
            time_diff = time() - self.bottom_wells_reset_last_time

            if time_diff > WELLS_ADJUST_RESET_TIMEOUT:
                should_reset_bottom = True

        if should_reset_top:
            self.top_wells = None
            self.top_wells_reset_last_time = None

        if should_reset_bottom:
            self.bottom_wells = None
            self.bottom_wells_reset_last_time = None

    def detect_top(self):
        processing_dictionary = {
            "scan_box_image": self.get_barcode_scanbox_image("top"),

            "barcode_x_size": self.settings.value("gui_elements/top_barcode_x_size_spinbox", type=int),
            "barcode_y_size": self.settings.value("gui_elements/top_barcode_y_size_spinbox", type=int),

            "threshold_center": self.settings.value("gui_elements/top_threshold_center_spinbox", type=int),
            "threshold_range": self.settings.value("gui_elements/top_threshold_range_spinbox", type=int),
        }

        detection_processor = DetectionProcessorCore.DetectionProcessor(processing_dictionary)
        detection_processor.process()

        if detection_processor.bardcode_found():
            barcode_data = detection_processor.get_barcode_data()

            output_image_group = [
                (barcode_data["original_image"].copy(),
                 self.image_mappings["settings_top_plate_tab"]["top_original_barcode_preview"]),
                (barcode_data["threshold_image"].copy(),
                 self.image_mappings["settings_top_plate_tab"]["top_threshold_barcode_preview"]),
            ]

            self.set_pixmap_from_image_groups_and_show(output_image_group)
            self.top_barcode_text_update_ready__signal.emit(barcode_data["barcode_value"])

        detection_processor.cleanup()

    def detect_bottom(self):
        processing_dictionary = {
            "scan_box_image": self.get_barcode_scanbox_image("bottom"),

            "barcode_x_size": self.settings.value("gui_elements/bottom_barcode_x_size_spinbox", type=int),
            "barcode_y_size": self.settings.value("gui_elements/bottom_barcode_y_size_spinbox", type=int),

            "threshold_center": self.settings.value("gui_elements/bottom_threshold_center_spinbox", type=int),
            "threshold_range": self.settings.value("gui_elements/bottom_threshold_range_spinbox", type=int),
        }

        detection_processor = DetectionProcessorCore.DetectionProcessor(processing_dictionary)
        detection_processor.process()

        if detection_processor.bardcode_found():
            barcode_data = detection_processor.get_barcode_data()

            output_image_group = [
                (barcode_data["original_image"].copy(),
                 self.image_mappings["settings_bottom_plate_tab"]["bottom_original_barcode_preview"]),
                (barcode_data["threshold_image"].copy(),
                 self.image_mappings["settings_bottom_plate_tab"]["bottom_threshold_barcode_preview"]),
            ]

            self.set_pixmap_from_image_groups_and_show(output_image_group)
            self.bottom_barcode_text_update_ready__signal.emit(barcode_data["barcode_value"])

        detection_processor.cleanup()

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
        wells_config = {
            "min_radius": self.settings.value("gui_elements/top_well_min_radius_spinbox", type=int),
            "max_radius": self.settings.value("gui_elements/top_well_max_radius_spinbox", type=int),
            "min_distance_between": self.settings.value("gui_elements/top_well_min_between_spinbox", type=int),
            "blur": self.settings.value("gui_elements/top_well_detection_blur_spinbox", type=int),
            "threshold_1": self.settings.value("gui_elements/top_well_detection_threshold_1_spinbox", type=int),
            "threshold_2": self.settings.value("gui_elements/top_well_detection_threshold_2_spinbox", type=int)
        }

        # ###### Get plate image from main preview
        top_plate_preview = self.get_plate_image("top")

        # ##### Get well preview and draw plate markers #####
        # Find wells
        if self.top_wells is None:
            self.progress_bar_status_update_requested__signal.emit(0)
            self.top_wells = ImageProcessing.find_wells_in_image(top_plate_preview, wells_config)
            self.progress_bar_status_update_requested__signal.emit(1)

        # Get well preview with barcode overlay, before we draw the wells overlay on main image
        well_preview = self.get_well_preview_image(top_plate_preview, self.top_wells)
        self.draw_barcode_overlay(well_preview, PREVIEW_EXAMPLE_TEXT, "top", "well")

        # Draw wells
        ImageProcessing.draw_wells_on_image(top_plate_preview, self.top_wells)

        # Draw barcode overlay
        self.draw_barcode_overlay(top_plate_preview, PREVIEW_EXAMPLE_TEXT, "top", "plate")

        output_image_group = [
            (top_plate_preview, self.image_mappings["settings_top_plate_tab"]["top_main_preview"]),
            (well_preview, self.image_mappings["settings_top_plate_tab"]["top_well_preview"])
        ]

        self.set_pixmap_from_image_groups_and_show(output_image_group)

    def show_bottom_plate_preview(self):
        wells_config = {
            "min_radius": self.settings.value("gui_elements/bottom_well_min_radius_spinbox", type=int),
            "max_radius": self.settings.value("gui_elements/bottom_well_max_radius_spinbox", type=int),
            "min_distance_between": self.settings.value("gui_elements/bottom_well_min_between_spinbox", type=int),
            "blur": self.settings.value("gui_elements/bottom_well_detection_blur_spinbox", type=int),
            "threshold_1": self.settings.value("gui_elements/bottom_well_detection_threshold_1_spinbox", type=int),
            "threshold_2": self.settings.value("gui_elements/bottom_well_detection_threshold_2_spinbox", type=int)
        }

        # ###### Get plate image from main preview
        bottom_plate_preview = self.get_plate_image("bottom")

        # ##### Get well preview and draw plate markers #####
        # Find wells
        if self.bottom_wells is None:
            self.progress_bar_status_update_requested__signal.emit(0)
            self.bottom_wells = ImageProcessing.find_wells_in_image(bottom_plate_preview, wells_config)
            self.progress_bar_status_update_requested__signal.emit(1)

        # Get well preview with barcode overlay, before we draw the wells overlay on main image
        well_preview = self.get_well_preview_image(bottom_plate_preview, self.bottom_wells)
        self.draw_barcode_overlay(well_preview, PREVIEW_EXAMPLE_TEXT, "bottom", "well")

        # Draw wells
        ImageProcessing.draw_wells_on_image(bottom_plate_preview, self.bottom_wells)

        # Draw barcode overlay
        self.draw_barcode_overlay(bottom_plate_preview, PREVIEW_EXAMPLE_TEXT, "bottom", "plate")

        # ##### Setup and show image group #####
        output_image_group = [
            (bottom_plate_preview, self.image_mappings["settings_bottom_plate_tab"]["bottom_main_preview"]),
            (well_preview, self.image_mappings["settings_bottom_plate_tab"]["bottom_well_preview"])
        ]

        self.set_pixmap_from_image_groups_and_show(output_image_group)

    def get_plate_image(self, top_or_bottom):
        plate_split_line_location = self.settings.value("gui_elements/alignment_shared_split_line_spinbox", type=int)

        preview_image = self.preview_image.copy()
        height, width, _ = preview_image.shape

        if top_or_bottom == "top":
            return preview_image[0:height, 0:plate_split_line_location]
        elif top_or_bottom == "bottom":
            return preview_image[0:height, plate_split_line_location:width]

    def get_well_preview_image(self, image, wells):
        if wells is not None:
            a1_well = wells[0]
            x, y, radius = a1_well

            size_scaled = int(radius * WELL_PREVIEW_BOX_SCALAR)

            well_left = x - size_scaled
            well_right = x + size_scaled
            well_top = y - size_scaled
            well_bottom = y + size_scaled

            return image[well_top:well_bottom, well_left:well_right].copy()

        return None

    def get_barcode_scanbox_image(self, top_or_bottom):
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

        return self.get_plate_image(top_or_bottom)[pt1_y:pt2_y, pt1_x:pt2_x].copy()

    def draw_wells_and_boxes(self, image, top_or_bottom):
        a1_x_location = self.settings.value("gui_elements/%s_a1_x_spinbox" % top_or_bottom, type=int)
        a1_y_location = self.settings.value("gui_elements/%s_a1_y_spinbox" % top_or_bottom, type=int)
        h12_x_location = self.settings.value("gui_elements/%s_h12_x_spinbox" % top_or_bottom, type=int)
        h12_y_location = self.settings.value("gui_elements/%s_h12_y_spinbox" % top_or_bottom, type=int)

        scanbox_x_position_spinbox = self.settings.value("gui_elements/%s_scanbox_x_position_spinbox" % top_or_bottom,
                                                         type=int)
        scanbox_y_position_spinbox = self.settings.value("gui_elements/%s_scanbox_y_position_spinbox" % top_or_bottom,
                                                         type=int)
        scanbox_x_size_spinbox = self.settings.value("gui_elements/%s_scanbox_x_size_spinbox" % top_or_bottom, type=int)
        scanbox_y_size_spinbox = self.settings.value("gui_elements/%s_scanbox_y_size_spinbox" % top_or_bottom, type=int)
        barcode_x_size_spinbox = self.settings.value("gui_elements/%s_barcode_x_size_spinbox" % top_or_bottom, type=int)
        barcode_y_size_spinbox = self.settings.value("gui_elements/%s_barcode_y_size_spinbox" % top_or_bottom, type=int)

        scan_box_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["scan_box"]["color"]
        scan_box_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["scan_box"]["thickness"]
        barcode_box_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["barcode_box"]["color"]
        barcode_box_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["barcode_box"]["thickness"]

        well_radius = self.settings.value("gui_elements/%s_well_radius_spinbox" % top_or_bottom, type=int)
        well_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["color"]
        well_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["thickness"]
        well_marker_color = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_marker_wells"]["color"]
        well_marker_thickness = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_marker_wells"]["thickness"]

        num_rows = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["rows"]
        num_columns = Constants.PREVIEW_IMAGE_DRAW_SETTINGS["plate_wells"]["columns"]

        # ##### Boxes #####
        # Scan box
        pt1_x = scanbox_x_position_spinbox - (scanbox_x_size_spinbox // 2)
        pt1_y = scanbox_y_position_spinbox - (scanbox_y_size_spinbox // 2)

        pt2_x = scanbox_x_position_spinbox + (scanbox_x_size_spinbox // 2)
        pt2_y = scanbox_y_position_spinbox + (scanbox_y_size_spinbox // 2)

        cv2.rectangle(image, (pt1_x, pt1_y), (pt2_x, pt2_y), scan_box_color, scan_box_thickness,
                      cv2.LINE_AA)

        # Barcode box
        pt1_x = scanbox_x_position_spinbox - (barcode_x_size_spinbox // 2)
        pt1_y = scanbox_y_position_spinbox - (barcode_y_size_spinbox // 2)

        pt2_x = scanbox_x_position_spinbox + (barcode_x_size_spinbox // 2)
        pt2_y = scanbox_y_position_spinbox + (barcode_y_size_spinbox // 2)

        cv2.rectangle(image, (pt1_x, pt1_y), (pt2_x, pt2_y), barcode_box_color, barcode_box_thickness,
                      cv2.LINE_AA)

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
        except IndexError:
            self.logger.debug("Could not remove marker wells. ")

        for location in locations:
            cv2.circle(image, location, well_radius, well_color, well_thickness, cv2.LINE_AA)

        cv2.circle(image, (a1_x_location, a1_y_location), well_radius, well_marker_color,
                   well_marker_thickness, cv2.LINE_AA)
        cv2.circle(image, (h12_x_location, h12_y_location), well_radius, well_marker_color,
                   well_marker_thickness, cv2.LINE_AA)

    def draw_barcode_overlay(self, image, text, top_or_bottom, plate_or_well):
        font_size = self.settings.value("gui_elements/%s_overlay_%s_font_size_spinbox" % (top_or_bottom, plate_or_well), type=int)
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
            print(e)

    # noinspection PyArgumentList
    def set_pixmap_from_image_groups_and_show(self, output_image_group):
        self.output_pixmap_groups = []

        for image_group in output_image_group:
            resized_pixmap = QtGui.QPixmap.fromImage(
                qimage2ndarray.array2qimage(cv2.resize(image_group[0], image_group[1]["size"])))
            self.output_pixmap_groups.append((resized_pixmap, image_group[1]["element"]))

        self.request_image_update__signal.emit()

    def on_top_well_detection_adjusted__slot(self):
        self.top_wells_reset_last_time = time()

    def on_bottom_well_detection_adjusted__slot(self):
        self.bottom_wells_reset_last_time = time()

    def on_continous_detect_checkbox_changed__slot(self, state):
        self.detect_continuous = state

    def on_single_detect_button_pressed__slot(self):
        self.detect_once = True

    def on_preview_image_path_changed__slot(self):
        self.attempted_preview_image_load = False
        self.preview_image_path_changed = True

    def on_image_update_requested__slot(self):
        for pixmap_group in self.output_pixmap_groups:
            try:
                pixmap_group[1].setPixmap(pixmap_group[0])
            except Exception as e:
                print(e)
        self.output_pixmap_groups = []

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        self.preview_image_path_line_edit.textChanged.connect(self.on_preview_image_path_changed__slot)

        self.continuous_detection_checkbox.stateChanged.connect(self.on_continous_detect_checkbox_changed__slot)
        self.single_detection_button.clicked.connect(self.on_single_detect_button_pressed__slot)

        self.top_barcode_text_update_ready__signal.connect(self.top_plate_barcode_value_label.setText)
        self.bottom_barcode_text_update_ready__signal.connect(self.bottom_plate_barcode_value_label.setText)

        self.top_well_min_radius_spinbox.valueChanged.connect(self.on_top_well_detection_adjusted__slot)
        self.top_well_max_radius_spinbox.valueChanged.connect(self.on_top_well_detection_adjusted__slot)
        self.top_well_min_between_spinbox.valueChanged.connect(self.on_top_well_detection_adjusted__slot)
        self.top_well_detection_blur_spinbox.valueChanged.connect(self.on_top_well_detection_adjusted__slot)
        self.top_well_detection_threshold_1_spinbox.valueChanged.connect(self.on_top_well_detection_adjusted__slot)
        self.top_well_detection_threshold_2_spinbox.valueChanged.connect(self.on_top_well_detection_adjusted__slot)

        self.bottom_well_min_radius_spinbox.valueChanged.connect(self.on_bottom_well_detection_adjusted__slot)
        self.bottom_well_max_radius_spinbox.valueChanged.connect(self.on_bottom_well_detection_adjusted__slot)
        self.bottom_well_min_between_spinbox.valueChanged.connect(self.on_bottom_well_detection_adjusted__slot)
        self.bottom_well_detection_blur_spinbox.valueChanged.connect(self.on_bottom_well_detection_adjusted__slot)
        self.bottom_well_detection_threshold_1_spinbox.valueChanged.connect(self.on_bottom_well_detection_adjusted__slot)
        self.bottom_well_detection_threshold_2_spinbox.valueChanged.connect(self.on_bottom_well_detection_adjusted__slot)

        self.progress_bar_status_update_requested__signal.connect(self.processing_progress_bar.setMaximum)

        self.request_image_update__signal.connect(self.on_image_update_requested__slot)

    def on_kill_threads__slot(self):
        self.run_thread_flag = False

    def setup_signals(self):
        self.core_signals["start"].connect(self.start)
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)
