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
from PyQt5 import QtCore, QtWidgets, QtGui
import logging


#####################################
# Detection Settings Class Definition
#####################################
class DetectionSettings(QtCore.QObject):

    image_update_needed_signal = QtCore.pyqtSignal()

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
        self.preview_image_load_b = self.main_window.detection_load_new_image_button  # type: QtWidgets.QPushButton
        self.preview_process_b = self.main_window.detection_process_button  # type: QtWidgets.QPushButton

        self.align_shared_split_sb = self.main_window.alignment_shared_split_line_spin_box  # type: QtWidgets.QSpinBox

        self.align_top_top_y_sb = self.main_window.alignment_top_top_row_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_top_left_x_sb = self.main_window.alignment_top_top_left_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_top_right_x_sb = self.main_window.alignment_top_top_right_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_bottom_y_sb = self.main_window.alignment_top_bottom_row_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_bottom_left_x_sb = self.main_window.alignment_top_bottom_left_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_top_bottom_right_x_sb = self.main_window.alignment_top_bottom_right_x_position_spin_box  # type: QtWidgets.QSpinBox

        self.align_bottom_top_y_sb = self.main_window.alignment_bottom_top_row_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_top_left_x_sb = self.main_window.alignment_bottom_top_left_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_top_right_x_sb = self.main_window.alignment_bottom_top_right_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_bottom_y_sb = self.main_window.alignment_bottom_bottom_row_y_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_bottom_left_x_sb = self.main_window.alignment_bottom_bottom_left_x_position_spin_box  # type: QtWidgets.QSpinBox
        self.align_bottom_bottom_right_x_sb = self.main_window.alignment_bottom_bottom_right_x_position_spin_box  # type: QtWidgets.QSpinBox

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
        # Load settings or load defaults
        shared_split = self.settings.value("detection_settings/alignment_and_limits/shared/split_value", 12085, type=int)

        align_top_top_y = self.settings.value("detection_settings/alignment_and_limits/top/top_y", 1022, type=int)
        align_top_top_left_x = self.settings.value("detection_settings/alignment_and_limits/top/top_left_x", 1130, type=int)
        align_top_top_right_x = self.settings.value("detection_settings/alignment_and_limits/top/top_right_x", 6910, type=int)
        align_top_bottom_y = self.settings.value("detection_settings/alignment_and_limits/top/bottom_y", 10340, type=int)
        align_top_bottom_left_x = self.settings.value("detection_settings/alignment_and_limits/top/bottom_left_x", 1130, type=int)
        align_top_bottom_right_x = self.settings.value("detection_settings/alignment_and_limits/top/bottom_right_x", 6910, type=int)

        align_bottom_top_y = self.settings.value("detection_settings/alignment_and_limits/bottom/top_y", 1010, type=int)
        align_bottom_top_left_x = self.settings.value("detection_settings/alignment_and_limits/bottom/top_left_x", 1130, type=int)
        align_bottom_top_right_x = self.settings.value("detection_settings/alignment_and_limits/bottom/top_right_x", 6910, type=int)
        align_bottom_bottom_y = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_y", 10340, type=int)
        align_bottom_bottom_left_x = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_left_x", 1130, type=int)
        align_bottom_bottom_right_x = self.settings.value("detection_settings/alignment_and_limits/bottom/bottom_right_x", 6910, type=int)

        detect_set_top_bc_x_size = self.settings.value("detection_settings/barcode_detection/top/barcode_x_size", 4600, type=int)
        detect_set_top_bc_y_size = self.settings.value("detection_settings/barcode_detection/top/barcode_y_size", 750, type=int)
        detect_set_top_scan_x_size = self.settings.value("detection_settings/barcode_detection/top/scan_x_size", 6650, type=int)
        detect_set_top_scan_y_size = self.settings.value("detection_settings/barcode_detection/top/scan_y_size", 1000, type=int)
        detect_set_top_scan_x_pos = self.settings.value("detection_settings/barcode_detection/top/scan_x_position", 4032, type=int)
        detect_set_top_scan_y_pos = self.settings.value("detection_settings/barcode_detection/top/scan_y_position", 11115, type=int)
        detect_set_top_scan_thresh_center = self.settings.value("detection_settings/barcode_detection/top/threshold_center", 128, type=int)
        detect_set_top_scan_thresh_range = self.settings.value("detection_settings/barcode_detection/top/threshold_range", 5, type=int)

        detect_set_bottom_bc_x_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_x_size", 4600, type=int)
        detect_set_bottom_bc_y_size = self.settings.value("detection_settings/barcode_detection/bottom/barcode_y_size", 750, type=int)
        detect_set_bottom_scan_x_size = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_size", 6650, type=int)
        detect_set_bottom_scan_y_size = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_size", 1000, type=int)
        detect_set_bottom_scan_x_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_x_position", 4032, type=int)
        detect_set_bottom_scan_y_pos = self.settings.value("detection_settings/barcode_detection/bottom/scan_y_position", 11115, type=int)
        detect_set_bottom_scan_thresh_center = self.settings.value("detection_settings/barcode_detection/bottom/threshold_center", 128, type=int)
        detect_set_bottom_scan_thresh_range = self.settings.value("detection_settings/barcode_detection/bottom/threshold_range", 5, type=int)

        # Set gui elements to their settings values
        self.align_shared_split_sb.setValue(shared_split)

        self.align_top_top_y_sb.setValue(align_top_top_y)
        self.align_top_top_left_x_sb.setValue(align_top_top_left_x)
        self.align_top_top_right_x_sb.setValue(align_top_top_right_x)
        self.align_top_bottom_y_sb.setValue(align_top_bottom_y)
        self.align_top_bottom_left_x_sb.setValue(align_top_bottom_left_x)
        self.align_top_bottom_right_x_sb.setValue(align_top_bottom_right_x)

        self.align_bottom_top_y_sb.setValue(align_bottom_top_y)
        self.align_bottom_top_left_x_sb.setValue(align_bottom_top_left_x)
        self.align_bottom_top_right_x_sb.setValue(align_bottom_top_right_x)
        self.align_bottom_bottom_y_sb.setValue(align_bottom_bottom_y)
        self.align_bottom_bottom_left_x_sb.setValue(align_bottom_bottom_left_x)
        self.align_bottom_bottom_right_x_sb.setValue(align_bottom_bottom_right_x)

        self.detect_set_top_bc_x_size_sb.setValue(detect_set_top_bc_x_size)
        self.detect_set_top_bc_y_size_sb.setValue(detect_set_top_bc_y_size)
        self.detect_set_top_scan_x_size_sb.setValue(detect_set_top_scan_x_size)
        self.detect_set_top_scan_y_size_sb.setValue(detect_set_top_scan_y_size)
        self.detect_set_top_scan_x_pos_sb.setValue(detect_set_top_scan_x_pos)
        self.detect_set_top_scan_y_pos_sb.setValue(detect_set_top_scan_y_pos)
        self.detect_set_top_scan_thresh_center_sb.setValue(detect_set_top_scan_thresh_center)
        self.detect_set_top_scan_thresh_range_sb.setValue(detect_set_top_scan_thresh_range)

        self.detect_set_bottom_bc_x_size_sb.setValue(detect_set_bottom_bc_x_size)
        self.detect_set_bottom_bc_y_size_sb.setValue(detect_set_bottom_bc_y_size)
        self.detect_set_bottom_scan_x_size_sb.setValue(detect_set_bottom_scan_x_size)
        self.detect_set_bottom_scan_y_size_sb.setValue(detect_set_bottom_scan_y_size)
        self.detect_set_bottom_scan_x_pos_sb.setValue(detect_set_bottom_scan_x_pos)
        self.detect_set_bottom_scan_y_pos_sb.setValue(detect_set_bottom_scan_y_pos)
        self.detect_set_bottom_scan_thresh_center_sb.setValue(detect_set_bottom_scan_thresh_center)
        self.detect_set_bottom_scan_thresh_range_sb.setValue(detect_set_bottom_scan_thresh_range)

        self.__on_settings_changed__slot()

    # noinspection PyUnresolvedReferences
    def __connect_signals_to_slots(self):
        self.align_shared_split_sb.valueChanged.connect(self.__on_settings_changed__slot)

        self.align_top_top_y_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_top_top_left_x_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_top_top_right_x_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_top_bottom_y_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_top_bottom_left_x_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_top_bottom_right_x_sb.valueChanged.connect(self.__on_settings_changed__slot)

        self.align_bottom_top_y_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_bottom_top_left_x_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_bottom_top_right_x_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_bottom_bottom_y_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_bottom_bottom_left_x_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.align_bottom_bottom_right_x_sb.valueChanged.connect(self.__on_settings_changed__slot)

        self.detect_set_top_bc_x_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_bc_y_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_scan_x_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_scan_y_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_scan_x_pos_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_scan_y_pos_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_scan_thresh_center_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_top_scan_thresh_range_sb.valueChanged.connect(self.__on_settings_changed__slot)

        self.detect_set_bottom_bc_x_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_bc_y_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_scan_x_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_scan_y_size_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_scan_x_pos_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_scan_y_pos_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_scan_thresh_center_sb.valueChanged.connect(self.__on_settings_changed__slot)
        self.detect_set_bottom_scan_thresh_range_sb.valueChanged.connect(self.__on_settings_changed__slot)

        self.preview_image_load_b.clicked.connect(self.__on_detection_load_preview_image_button_clicked__slot)
        self.preview_process_b.clicked.connect(self.__on_process_button_clicked__slot)

    def __on_settings_changed__slot(self):
        self.settings.setValue("detection_settings/alignment_and_limits/shared/split_value", self.align_shared_split_sb.value())

        self.settings.setValue("detection_settings/alignment_and_limits/top/top_y", self.align_top_top_y_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/top/top_left_x", self.align_top_top_left_x_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/top/top_right_x", self.align_top_top_right_x_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/top/bottom_y", self.align_top_bottom_y_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/top/bottom_left_x", self.align_top_bottom_left_x_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/top/bottom_right_x", self.align_top_bottom_right_x_sb.value())

        self.settings.setValue("detection_settings/alignment_and_limits/bottom/top_y", self.align_bottom_top_y_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/bottom/top_left_x", self.align_bottom_top_left_x_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/bottom/top_right_x", self.align_bottom_top_right_x_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/bottom/bottom_y", self.align_bottom_bottom_y_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/bottom/bottom_left_x", self.align_bottom_bottom_left_x_sb.value())
        self.settings.setValue("detection_settings/alignment_and_limits/bottom/bottom_right_x", self.align_bottom_bottom_right_x_sb.value())

        self.settings.setValue("detection_settings/barcode_detection/top/barcode_x_size", self.detect_set_top_bc_x_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/barcode_y_size", self.detect_set_top_bc_y_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/scan_x_size", self.detect_set_top_scan_x_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/scan_y_size", self.detect_set_top_scan_y_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/scan_x_position", self.detect_set_top_scan_x_pos_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/scan_y_position", self.detect_set_top_scan_y_pos_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/threshold_center", self.detect_set_top_scan_thresh_center_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/top/threshold_range", self.detect_set_top_scan_thresh_range_sb.value())

        self.settings.setValue("detection_settings/barcode_detection/bottom/barcode_x_size", self.detect_set_bottom_bc_x_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/barcode_y_size", self.detect_set_bottom_bc_y_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/scan_x_size", self.detect_set_bottom_scan_x_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/scan_y_size", self.detect_set_bottom_scan_y_size_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/scan_x_position", self.detect_set_bottom_scan_x_pos_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/scan_y_position", self.detect_set_bottom_scan_y_pos_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/threshold_center", self.detect_set_bottom_scan_thresh_center_sb.value())
        self.settings.setValue("detection_settings/barcode_detection/bottom/threshold_range", self.detect_set_bottom_scan_thresh_range_sb.value())

        self.logger.debug("Detection settings changes saved...")

    # noinspection PyArgumentList
    def __on_detection_load_preview_image_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        file_path = file_dialog.getOpenFileName()[0]

        if file_path != "":
            self.settings.setValue("detection_settings/preview_image_path", file_path)
            self.logger.debug("Setting preview image path to: \"" + file_path + "\".")

            self.image_update_needed_signal.emit()
        else:
            self.logger.debug("Preview image path not changed. No file selected.")

    def __on_process_button_clicked__slot(self):
        self.image_update_needed_signal.emit()

    # noinspection PyCallByClass,PyArgumentList,PyTypeChecker
    def on_preview_images_ready__slot(self):
        main_pixmap = self.main_window.detection_preview_class.detection_main_preview_pixmap  # type: QtGui.QPixmap

        top_raw_pixmap = self.main_window.detection_preview_class.detection_top_bc_raw_preview_pixmap  # type: QtGui.QPixmap
        top_threshold_pixmap = self.main_window.detection_preview_class.detection_top_bc_threshold_preview_pixmap  # type: QtGui.QPixmap
        top_barcode_string = self.main_window.detection_preview_class.detection_top_bc_string  # type: str

        bottom_raw_pixmap = self.main_window.detection_preview_class.detection_bottom_bc_raw_preview_pixmap  # type: QtGui.QPixmap
        bottom_threshold_pixmap = self.main_window.detection_preview_class.detection_bottom_bc_threshold_preview_pixmap  # type: QtGui.QPixmap
        bottom_barcode_string = self.main_window.detection_preview_class.detection_bottom_bc_string  # type: str

        try:
            self.preview_image_lb.setPixmap(main_pixmap)

            self.detect_prev_top_raw_lb.setPixmap(top_raw_pixmap)
            self.detect_prev_top_thresh_lb.setPixmap(top_threshold_pixmap)
            self.detect_prev_top_bc_lb.setText(top_barcode_string)

            self.detect_prev_bottom_raw_lb.setPixmap(bottom_raw_pixmap)
            self.detect_prev_bottom_thresh_lb.setPixmap(bottom_threshold_pixmap)
            self.detect_prev_bottom_bc_lb.setText(bottom_barcode_string)

        except:
            pass