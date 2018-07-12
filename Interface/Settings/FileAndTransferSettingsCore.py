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
# File and Transfer Class Definition
#####################################
class FileAndTransferSettings(QtCore.QObject):

    file_and_transfer_settings_changed_signal = QtCore.pyqtSignal()

    def __init__(self, main_window):
        super(FileAndTransferSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window  # type: QtWidgets.QMainWindow

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## References to GUI Elements ##########
        self.input_images_le = self.main_window.file_transfer_input_images_line_edit  # type: QtWidgets.QLineEdit
        self.failed_rename_le = self.main_window.file_transfer_failed_rename_images_line_edit  # type: QtWidgets.QLineEdit
        self.local_output_le = self.main_window.file_transfer_local_output_line_edit  # type: QtWidgets.QLineEdit
        self.network_transfer_le = self.main_window.file_transfer_network_transfer_line_edit  # type: QtWidgets.QLineEdit
        self.zbar_path_le = self.main_window.file_transfer_zbar_path_line_edit  # type: QtWidgets.QLineEdit

        self.input_images_browse_b = self.main_window.file_transfer_input_images_browse_button  # type: QtWidgets.QPushButton
        self.failed_rename_browse_b = self.main_window.file_transfer_failed_rename_images_browse_button  # type: QtWidgets.QPushButton
        self.local_output_browse_b = self.main_window.file_transfer_local_output_browse_button  # type: QtWidgets.QPushButton
        self.network_transfer_browse_b = self.main_window.file_transfer_network_transfer_browse_button  # type: QtWidgets.QPushButton
        self.zbar_path_browse_b = self.main_window.file_transfer_zbar_path_browse_button  # type: QtWidgets.QPushButton

        self.transfer_time_te = self.main_window.file_transfer_transfer_time_edit  # type: QtWidgets.QTimeEdit

        # ########## Load Settings ##########
        self.__load_settings()

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

    def __load_settings(self):
        input_images_path = self.settings.value("file_and_transfer_settings/input_images_path",
                                                "*** No Path Set ***", type=str)
        failed_rename_path = self.settings.value("file_and_transfer_settings/failed_rename_path",
                                                 "*** No Path Set ***", type=str)
        local_output_path = self.settings.value("file_and_transfer_settings/local_output_path",
                                                "*** No Path Set ***", type=str)
        network_transfer_path = self.settings.value("file_and_transfer_settings/network_transfer_path",
                                                    "*** No Path Set ***", type=str)
        zbar_path = self.settings.value("file_and_transfer_settings/zbar_path",
                                        "*** No Path Set ***", type=str)
        transfer_time_string = self.settings.value("file_and_transfer_settings/network_transfer_time",
                                                   "12:00 PM", type=str)

        self.input_images_le.setText(input_images_path)
        self.failed_rename_le.setText(failed_rename_path)
        self.local_output_le.setText(local_output_path)
        self.network_transfer_le.setText(network_transfer_path)
        self.zbar_path_le.setText(zbar_path)
        self.transfer_time_te.setTime(QtCore.QTime.fromString(transfer_time_string, "h:mm AP"))

        self.__on_settings_changed__slot()

    # noinspection PyUnresolvedReferences
    def __connect_signals_to_slots(self):
        self.input_images_browse_b.clicked.connect(self.__on_input_images_browse_button_clicked__slot)
        self.failed_rename_browse_b.clicked.connect(self.__on_failed_rename_browse_button_clicked__slot)
        self.local_output_browse_b.clicked.connect(self.__on_local_output_browse_button_clicked__slot)
        self.network_transfer_browse_b.clicked.connect(self.__on_network_transfer_browse_button_clicked__slot)
        self.zbar_path_browse_b.clicked.connect(self.__on_zbar_browse_button_clicked__slot)

        self.input_images_le.textChanged.connect(self.__on_settings_changed__slot)
        self.failed_rename_le.textChanged.connect(self.__on_settings_changed__slot)
        self.local_output_le.textChanged.connect(self.__on_settings_changed__slot)
        self.network_transfer_le.textChanged.connect(self.__on_settings_changed__slot)
        self.zbar_path_le.textChanged.connect(self.__on_settings_changed__slot)

        self.transfer_time_te.timeChanged.connect(self.__on_settings_changed__slot)

    # noinspection PyArgumentList
    def __on_input_images_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_window)
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
        file_dialog = QtWidgets.QFileDialog(self.main_window)
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
        file_dialog = QtWidgets.QFileDialog(self.main_window)
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
        file_dialog = QtWidgets.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        directory = file_dialog.getExistingDirectory()

        if directory != "":
            self.network_transfer_le.setText(directory)
            self.logger.debug("Setting network transfer directory to: \"" + directory + "\".")
        else:
            self.logger.debug("Network transfer directory not changed. No folder selected.")

    # noinspection PyArgumentList
    def __on_zbar_browse_button_clicked__slot(self):
        file_dialog = QtWidgets.QFileDialog(self.main_window)
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        file_dialog.setDirectory(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.HomeLocation)[0])

        file_path = file_dialog.getOpenFileName(filter="zbarimg Executable (zbarimg.exe)")[0]

        if file_path != "":
            self.zbar_path_le.setText(file_path)
            self.logger.debug("Setting zbar executable path to: \"" + file_path + "\".")
        else:
            self.logger.debug("ZBar executable path not changed. No file selected.")

    def __on_settings_changed__slot(self):
        self.settings.setValue("file_and_transfer_settings/input_images_path", self.input_images_le.text())
        self.settings.setValue("file_and_transfer_settings/failed_rename_path", self.failed_rename_le.text())
        self.settings.setValue("file_and_transfer_settings/local_output_path", self.local_output_le.text())
        self.settings.setValue("file_and_transfer_settings/network_transfer_path", self.network_transfer_le.text())
        self.settings.setValue("file_and_transfer_settings/zbar_path", self.zbar_path_le.text())

        self.settings.setValue("file_and_transfer_settings/network_transfer_time",
                               self.transfer_time_te.time().toString('h:mm AP'))

        self.logger.debug("File and transfer settings changes saved...")
        self.file_and_transfer_settings_changed_signal.emit()

