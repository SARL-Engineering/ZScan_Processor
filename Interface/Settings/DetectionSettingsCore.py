#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging

# Custom imports
from Resources import Constants
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI


#####################################
# Detection Settings Class Definition
#####################################
class DetectionSettings(QtCore.QObject):

    image_update_needed_signal = QtCore.pyqtSignal()

    def __init__(self, shared_objects):
        super(DetectionSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## References to GUI Elements ##########
        # Plate Splitting
        self.alignment_shared_split_line_spinbox = self.main_screen.alignment_shared_split_line_spinbox  # type: QtWidgets.QSpinBox

        # Top Plate
        self.top_a1_x_spinbox = self.main_screen.top_a1_x_spinbox  # type: QtWidgets.QSpinBox
        self.top_a1_y_spinbox = self.main_screen.top_a1_y_spinbox  # type: QtWidgets.QSpinBox
        self.top_h12_x_spinbox = self.main_screen.top_h12_x_spinbox  # type: QtWidgets.QSpinBox
        self.top_h12_y_spinbox = self.main_screen.top_h12_y_spinbox  # type: QtWidgets.QSpinBox
        self.top_well_radius_spinbox = self.main_screen.top_well_radius_spinbox  # type: QtWidgets.QSpinBox

        self.top_barcode_x_size_spinbox = self.main_screen.top_barcode_x_size_spinbox  # type: QtWidgets.QSpinBox
        self.top_barcode_y_size_spinbox = self.main_screen.top_barcode_y_size_spinbox  # type: QtWidgets.QSpinBox
        self.top_scanbox_x_size_spinbox = self.main_screen.top_scanbox_x_size_spinbox  # type: QtWidgets.QSpinBox
        self.top_scanbox_y_size_spinbox = self.main_screen.top_scanbox_y_size_spinbox  # type: QtWidgets.QSpinBox
        self.top_scanbox_x_position_spinbox = self.main_screen.top_scanbox_x_position_spinbox  # type: QtWidgets.QSpinBox
        self.top_scanbox_y_position_spinbox = self.main_screen.top_scanbox_y_position_spinbox  # type: QtWidgets.QSpinBox

        self.top_threshold_center_spinbox = self.main_screen.top_threshold_center_spinbox  # type: QtWidgets.QSpinBox
        self.top_threshold_range_spinbox = self.main_screen.top_threshold_range_spinbox  # type: QtWidgets.QSpinBox

        self.top_overlay_plate_font_size_spinbox = self.main_screen.top_overlay_plate_font_size_spinbox  # type: QtWidgets.QSpinBox
        self.top_overlay_well_font_size_spinbox = self.main_screen.top_overlay_well_font_size_spinbox  # type: QtWidgets.QSpinBox

        # Bottom Plate
        self.bottom_a1_x_spinbox = self.main_screen.bottom_a1_x_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_a1_y_spinbox = self.main_screen.bottom_a1_y_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_h12_x_spinbox = self.main_screen.bottom_h12_x_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_h12_y_spinbox = self.main_screen.bottom_h12_y_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_well_radius_spinbox = self.main_screen.bottom_well_radius_spinbox  # type: QtWidgets.QSpinBox

        self.bottom_barcode_x_size_spinbox = self.main_screen.bottom_barcode_x_size_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_barcode_y_size_spinbox = self.main_screen.bottom_barcode_y_size_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_scanbox_x_size_spinbox = self.main_screen.bottom_scanbox_x_size_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_scanbox_y_size_spinbox = self.main_screen.bottom_scanbox_y_size_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_scanbox_x_position_spinbox = self.main_screen.bottom_scanbox_x_position_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_scanbox_y_position_spinbox = self.main_screen.bottom_scanbox_y_position_spinbox  # type: QtWidgets.QSpinBox

        self.bottom_threshold_center_spinbox = self.main_screen.bottom_threshold_center_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_threshold_range_spinbox = self.main_screen.bottom_threshold_range_spinbox  # type: QtWidgets.QSpinBox

        self.bottom_overlay_plate_font_size_spinbox = self.main_screen.bottom_overlay_plate_font_size_spinbox  # type: QtWidgets.QSpinBox
        self.bottom_overlay_well_font_size_spinbox = self.main_screen.bottom_overlay_well_font_size_spinbox  # type: QtWidgets.QSpinBox

        # ########## Load Settings ##########
        self.__load_settings()

        # ########## Prepare signal/slot connections ##########
        self.setup_signals()

    def __load_settings(self):
        # Load settings or load defaults
        for gui_element in Constants.DETECTION_SETTINGS_GUI_ELEMENTS:
            value_to_show = self.settings.value("gui_elements/" + gui_element, Constants.DETECTION_SETTINGS_GUI_ELEMENTS[gui_element])
            getattr(self, gui_element).setValue(value_to_show)

        self.__on_settings_changed__slot()

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        for gui_element in Constants.DETECTION_SETTINGS_GUI_ELEMENTS:
            current_widget = getattr(self, gui_element)

            if isinstance(current_widget, QtWidgets.QSpinBox):
                current_widget.valueChanged.connect(self.__on_settings_changed__slot)

    def __on_settings_changed__slot(self):
        for gui_element in Constants.DETECTION_SETTINGS_GUI_ELEMENTS:
            value_to_save = getattr(self, gui_element).value()
            self.settings.setValue("gui_elements/" + gui_element, value_to_save)

        self.logger.debug("Detection settings changes saved...")

    def setup_signals(self):
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)

