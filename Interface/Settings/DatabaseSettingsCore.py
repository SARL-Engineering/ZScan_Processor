#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging
import mysql.connector

# Custom imports
from Resources import Constants
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI


#####################################
# Detection Settings Class Definition
#####################################
class DatabaseSettings(QtCore.QObject):

    image_update_needed_signal = QtCore.pyqtSignal()

    def __init__(self, shared_objects):
        super(DatabaseSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## References to GUI Elements ##########
        self.database_host_line_edit = self.main_screen.database_host_line_edit  # type: QtWidgets.QLineEdit
        self.database_username_line_edit = self.main_screen.database_username_line_edit  # type: QtWidgets.QLineEdit
        self.database_password_line_edit = self.main_screen.database_password_line_edit  # type: QtWidgets.QLineEdit
        self.database_database_line_edit = self.main_screen.database_database_line_edit  # type: QtWidgets.QLineEdit
        self.database_insert_query_line_edit = self.main_screen.database_insert_query_line_edit  # type: QtWidgets.QLineEdit

        self.database_test_connection_button = self.main_screen.database_test_connection_button  # type: QtWidgets.QPushButton

        # ########## Load Settings ##########
        self.__load_settings()

        # ########## Prepare signal/slot connections ##########
        self.setup_signals()

    def on_test_connection_button_clicked__slot(self):
        host = self.settings.value("gui_elements/database_host_line_edit", type=str)
        username = self.settings.value("gui_elements/database_username_line_edit", type=str)
        password = self.settings.value("gui_elements/database_password_line_edit", type=str)
        database = self.settings.value("gui_elements/database_database_line_edit", type=str)

        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("Results")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)

        try:
            mysql.connector.connect(
                host=host,
                user=username,
                passwd=password,
                database=database
            )

            message_box.setIcon(QtWidgets.QMessageBox.Information)
            message_box.setText("Test successful!")
        except mysql.connector.Error as e:
            message_box.setIcon(QtWidgets.QMessageBox.Warning)
            message_box.setText("Test unsuccessful!")
            message_box.setInformativeText("Error was: %s" % e.msg)

        message_box.exec()

    def __load_settings(self):
        # Load settings or load defaults
        for gui_element in Constants.DATABASE_SETTINGS_GUI_ELEMENTS:
            value_to_show = self.settings.value("gui_elements/" + gui_element, Constants.DATABASE_SETTINGS_GUI_ELEMENTS[gui_element])
            getattr(self, gui_element).setText(value_to_show)

        self.__on_settings_changed__slot()

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        for gui_element in Constants.DATABASE_SETTINGS_GUI_ELEMENTS:
            current_widget = getattr(self, gui_element)
            current_widget.textChanged.connect(self.__on_settings_changed__slot)

        self.database_test_connection_button.clicked.connect(self.on_test_connection_button_clicked__slot)

    def __on_settings_changed__slot(self):
        for gui_element in Constants.DATABASE_SETTINGS_GUI_ELEMENTS:
            value_to_save = getattr(self, gui_element).text()
            self.settings.setValue("gui_elements/" + gui_element, value_to_save)

        self.logger.debug("Database settings changes saved...")

    def setup_signals(self):
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)

