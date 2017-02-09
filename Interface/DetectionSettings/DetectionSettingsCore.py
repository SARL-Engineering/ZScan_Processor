"""
    This file contains the file and transfer settings page sub-class
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
from PyQt5 import QtCore, QtWidgets
import logging

#####################################
# Detection Settings Class Definition
#####################################
class DetectionSettings(QtCore.QObject):
    def __init__(self, main_window):
        super(DetectionSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window  # type: QtWidgets.QMainWindow

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## References to GUI Elements ##########
        self.preview_image_lb = self.main_window.detection_main_preview_label  # type: QtWidgets.QLabel
        self.preview_image_load_b = self.main_window.detection_load_image_button  # type: QtWidgets.QPushButton

        self.align_shared_split_sb = self.main_window.alignment_shared_split_line_spin_box  # type: QtWidgets.QSpinBox

        self.align_top_bottom_y_sb = self.main_window.alignment_top_row_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_left_x_sb = self.main_window.alignment_top_left_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_right_x_sb = self.main_window.alignment_top_right_x_position_spin_box  # type: QtWidgets.QSpinBox

        self.align_bottom_bottom_y_sb = self.main_window.alignment_bottom_row_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_left_x_sb = self.main_window.alignment_bottom_left_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_right_x_sb = self.main_window.alignment_bottom_right_x_position_spin_box  # type: QtWidgets.QSpinBox

        self.detect_set_top_bc_x_size_sb = self.main_window.detection_top_barcode_x_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_bc_y_size_sb = self.main_window.detection_top_barcode_y_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_scan_x_size_sb = self.main_window.detection_top_scan_x_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_scan_y_size_sb = self.main_window.detection_top_scan_y_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_scan_x_pos_sb = self.main_window.detection_top_scan_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_scan_y_pos_sb = self.main_window.detection_top_scan_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_scan_thresh_center_sb = self.main_window.detection_top_threshold_center_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_top_scan_thresh_range_sb = self.main_window.detection_top_threshold_range_spin_box  # type: QtWidgets.QSpinBox

        self.detect_set_bottom_bc_x_size_sb = self.main_window.detection_bottom_barcode_x_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_bc_y_size_sb = self.main_window.detection_bottom_barcode_y_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_scan_x_size_sb = self.main_window.detection_bottom_scan_x_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_scan_y_size_sb = self.main_window.detection_bottom_scan_y_size_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_scan_x_pos_sb = self.main_window.detection_bottom_scan_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_scan_y_pos_sb = self.main_window.detection_bottom_scan_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_scan_thresh_center_sb = self.main_window.detection_bottom_threshold_center_spin_box  # type: QtWidgets.QSpinBox
        self.detect_set_bottom_scan_thresh_range_sb = self.main_window.detection_bottom_threshold_range_spin_box  # type: QtWidgets.QSpinBox

        self.detect_prev_top_raw_lb = self.main_window.barcode_preview_top_raw_label  # type: QtWidgets.QLabel
        self.detect_prev_top_thresh_lb = self.main_window.barcode_preview_top_threshold_label  # type: QtWidgets.QLabel
        self.detect_prev_top_bc_lb = self.main_window.barcode_preview_top_barcode_label  # type: QtWidgets.QLabel

        self.detect_prev_bottom_raw_lb = self.main_window.barcode_preview_bottom_raw_label  # type: QtWidgets.QLabel
        self.detect_prev_bottom_thresh_lb = self.main_window.barcode_preview_bottom_threshold_label  # type: QtWidgets.QLabel
        self.detect_prev_bottom_bc_lb = self.main_window.barcode_preview_bottom_barcode_label  # type: QtWidgets.QLabel

        # ########## Load Settings ##########
        self.__load_settings()

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

    def __load_settings(self):
        self.preview_image_lb

        self.align_shared_split_sb

        self.align_top_bottom_y_sb
        self.align_top_left_x_sb
        self.align_top_right_x_sb

        self.align_bottom_bottom_y_sb
        self.align_bottom_left_x_sb
        self.align_bottom_right_x_sb

        self.detect_set_top_bc_x_size_sb
        self.detect_set_top_bc_y_size_sb
        self.detect_set_top_scan_x_size_sb
        self.detect_set_top_scan_y_size_sb
        self.detect_set_top_scan_x_pos_sb
        self.detect_set_top_scan_y_pos_sb
        self.detect_set_top_scan_thresh_center_sb
        self.detect_set_top_scan_thresh_range_sb

        self.detect_set_bottom_bc_x_size_sb
        self.detect_set_bottom_bc_y_size_sb
        self.detect_set_bottom_scan_x_size_sb
        self.detect_set_bottom_scan_y_size_sb
        self.detect_set_bottom_scan_x_pos_sb
        self.detect_set_bottom_scan_y_pos_sb
        self.detect_set_bottom_scan_thresh_center_sb
        self.detect_set_bottom_scan_thresh_range_sb

        self.settings.value("detection_settings/top_bc_preview_image_path",
                            "Resources/UI/preview_please_load_image_barcode.png")
        self.detect_prev_top_raw_lb
        self.detect_prev_top_thresh_lb
        self.detect_prev_top_bc_lb

        self.settings.value("detection_settings/bottom_bc_preview_image_path",
                            "Resources/UI/preview_please_load_image_barcode.png")
        self.detect_prev_bottom_raw_lb
        self.detect_prev_bottom_thresh_lb
        self.detect_prev_bottom_bc_lb

    def __on_settings_changed__slot(self):
        self.align_shared_split_sb

        self.align_top_bottom_y_sb
        self.align_top_left_x_sb
        self.align_top_right_x_sb

        self.align_bottom_bottom_y_sb
        self.align_bottom_left_x_sb
        self.align_bottom_right_x_sb

        self.detect_set_top_bc_x_size_sb
        self.detect_set_top_bc_y_size_sb
        self.detect_set_top_scan_x_size_sb
        self.detect_set_top_scan_y_size_sb
        self.detect_set_top_scan_x_pos_sb
        self.detect_set_top_scan_y_pos_sb
        self.detect_set_top_scan_thresh_center_sb
        self.detect_set_top_scan_thresh_range_sb

        self.detect_set_bottom_bc_x_size_sb
        self.detect_set_bottom_bc_y_size_sb
        self.detect_set_bottom_scan_x_size_sb
        self.detect_set_bottom_scan_y_size_sb
        self.detect_set_bottom_scan_x_pos_sb
        self.detect_set_bottom_scan_y_pos_sb
        self.detect_set_bottom_scan_thresh_center_sb
        self.detect_set_bottom_scan_thresh_range_sb

    def __connect_signals_to_slots(self):
        pass
