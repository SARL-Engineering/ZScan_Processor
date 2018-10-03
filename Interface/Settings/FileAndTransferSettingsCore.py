#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets
import logging

# Custom imports
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI


#####################################
# File and Transfer Class Definition
#####################################
class FileAndTransferSettings(QtCore.QObject):

    file_and_transfer_settings_changed_signal = QtCore.pyqtSignal()

    def __init__(self, shared_objects):
        super(FileAndTransferSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## References to GUI Elements ##########
        self.input_images_le = self.main_screen.file_transfer_input_images_line_edit  # type: QtWidgets.QLineEdit
        self.failed_rename_le = self.main_screen.file_transfer_failed_rename_images_line_edit  # type: QtWidgets.QLineEdit
        self.local_output_le = self.main_screen.file_transfer_local_output_line_edit  # type: QtWidgets.QLineEdit
        self.network_transfer_le = self.main_screen.file_transfer_network_transfer_line_edit  # type: QtWidgets.QLineEdit

        self.input_images_browse_b = self.main_screen.file_transfer_input_images_browse_button  # type: QtWidgets.QPushButton
        self.failed_rename_browse_b = self.main_screen.file_transfer_failed_rename_images_browse_button  # type: QtWidgets.QPushButton
        self.local_output_browse_b = self.main_screen.file_transfer_local_output_browse_button  # type: QtWidgets.QPushButton
        self.network_transfer_browse_b = self.main_screen.file_transfer_network_transfer_browse_button  # type: QtWidgets.QPushButton

        self.transfer_time_te = self.main_screen.file_transfer_transfer_time_edit  # type: QtWidgets.QTimeEdit

        self.set_preview_image_browse_b = self.main_screen.set_preview_image_browse_b  # type: QtWidgets.QPushButton
        self.preview_image_path_le = self.main_screen.preview_image_path_line_edit  # type: QtWidgets.QLineEdit
        self.preview_image_x_size_lb = self.main_screen.preview_image_x_size_label  # type: QtWidgets.QLabel
        self.preview_image_y_size_lb = self.main_screen.preview_image_y_size_label  # type: QtWidgets.QLabel
        self.preview_image_file_size_lb = self.main_screen.preview_image_file_size_label  # type: QtWidgets.QLabel

        # ########## Load Settings ##########
        self.__load_settings()

        # ########## Prepare signal/slot connections ##########
        self.setup_signals()

    def __load_settings(self):
        input_images_path = self.settings.value("file_and_transfer_settings/input_images_path",
                                                "*** No Path Set ***", type=str)
        failed_rename_path = self.settings.value("file_and_transfer_settings/failed_rename_path",
                                                 "*** No Path Set ***", type=str)
        local_output_path = self.settings.value("file_and_transfer_settings/local_output_path",
                                                "*** No Path Set ***", type=str)
        network_transfer_path = self.settings.value("file_and_transfer_settings/network_transfer_path",
                                                    "*** No Path Set ***", type=str)
        transfer_time_string = self.settings.value("file_and_transfer_settings/network_transfer_time",
                                                   "12:00 PM", type=str)

        preview_image_path = self.settings.value("file_and_transfer_settings/preview_image_path",
                                                    "*** No Path Set ***", type=str)

        self.input_images_le.setText(input_images_path)
        self.failed_rename_le.setText(failed_rename_path)
        self.local_output_le.setText(local_output_path)
        self.network_transfer_le.setText(network_transfer_path)
        self.transfer_time_te.setTime(QtCore.QTime.fromString(transfer_time_string, "h:mm AP"))

        self.preview_image_path_le.setText(preview_image_path)

        self.__on_settings_changed__slot()

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        self.input_images_browse_b.clicked.connect(self.__on_input_images_browse_button_clicked__slot)
        self.failed_rename_browse_b.clicked.connect(self.__on_failed_rename_browse_button_clicked__slot)
        self.local_output_browse_b.clicked.connect(self.__on_local_output_browse_button_clicked__slot)
        self.network_transfer_browse_b.clicked.connect(self.__on_network_transfer_browse_button_clicked__slot)

        self.input_images_le.textChanged.connect(self.__on_settings_changed__slot)
        self.failed_rename_le.textChanged.connect(self.__on_settings_changed__slot)
        self.local_output_le.textChanged.connect(self.__on_settings_changed__slot)
        self.network_transfer_le.textChanged.connect(self.__on_settings_changed__slot)

        self.transfer_time_te.timeChanged.connect(self.__on_settings_changed__slot)

        self.set_preview_image_browse_b.clicked.connect(self.__on_set_preview_image_browse_button_clicked__slot)
        self.preview_image_path_le.textChanged.connect(self.__on_settings_changed__slot)

    def setup_signals(self):
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)

    # noinspection PyArgumentList
    def __on_input_images_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_screen)
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        directory = file_dialog.getExistingDirectory()

        if directory != "":
            self.input_images_le.setText(directory)
            self.logger.debug("Setting input images directory to: \"" + directory + "\".")
        else:
            self.logger.debug("Input images directory not changed. No folder selected.")

    # noinspection PyArgumentList
    def __on_failed_rename_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_screen)
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        directory = file_dialog.getExistingDirectory()

        if directory != "":
            self.failed_rename_le.setText(directory)
            self.logger.debug("Setting failed rename directory to: \"" + directory + "\".")
        else:
            self.logger.debug("Failed rename directory not changed. No folder selected.")

    # noinspection PyArgumentList
    def __on_local_output_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_screen)
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        directory = file_dialog.getExistingDirectory()

        if directory != "":
            self.local_output_le.setText(directory)
            self.logger.debug("Setting local output directory to: \"" + directory + "\".")
        else:
            self.logger.debug("Local output directory not changed. No folder selected.")

    # noinspection PyArgumentList
    def __on_network_transfer_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_screen)
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        directory = file_dialog.getExistingDirectory()

        if directory != "":
            self.network_transfer_le.setText(directory)
            self.logger.debug("Setting network transfer directory to: \"" + directory + "\".")
        else:
            self.logger.debug("Network transfer directory not changed. No folder selected.")

    # noinspection PyArgumentList
    def __on_set_preview_image_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_screen)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        last_directory = self.settings.value("file_and_transfer_settings/preview_image_directory", None)

        if last_directory:
            file_dialog.setDirectory(last_directory)
        else:
            file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        file_name = file_dialog.getOpenFileName()[0]

        if file_name != "":
            self.preview_image_path_le.setText(file_name)
            self.logger.debug("Setting preview image path to: \"" + file_name + "\".")

            file_directory = QtCore.QFileInfo(file_name).absoluteDir().absolutePath()
            self.settings.setValue("file_and_transfer_settings/preview_image_directory", file_directory)
        else:
            self.logger.debug("Preview image path not changed. No file selected.")

    def __on_settings_changed__slot(self):
        self.settings.setValue("file_and_transfer_settings/input_images_path", self.input_images_le.text())
        self.settings.setValue("file_and_transfer_settings/failed_rename_path", self.failed_rename_le.text())
        self.settings.setValue("file_and_transfer_settings/local_output_path", self.local_output_le.text())
        self.settings.setValue("file_and_transfer_settings/network_transfer_path", self.network_transfer_le.text())

        self.settings.setValue("file_and_transfer_settings/network_transfer_time",
                               self.transfer_time_te.time().toString('h:mm AP'))

        self.settings.setValue("file_and_transfer_settings/preview_image_path", self.preview_image_path_le.text())

        self.logger.debug("File and transfer settings changes saved...")
        self.file_and_transfer_settings_changed_signal.emit()

