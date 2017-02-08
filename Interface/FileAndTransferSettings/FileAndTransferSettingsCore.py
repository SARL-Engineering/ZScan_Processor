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


#####################################
# File and Transfer Class Definition
#####################################
class FileAndTransferSettings(QtCore.QObject):
    def __init__(self, main_window):
        super(FileAndTransferSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## References to GUI Elements ##########
        self.input_images_le = self.main_window.file_transfer_input_images_line_edit  # type: QtWidgets.QLineEdit
        self.failed_rename_le = self.main_window.file_transfer_failed_rename_images_line_edit  # type: QtWidgets.QLineEdit
        self.local_output_le = self.main_window.file_transfer_local_output_line_edit  # type: QtWidgets.QLineEdit
        self.network_transfer_le = self.main_window.file_transfer_network_transfer_line_edit  # type: QtWidgets.QLineEdit

        self.input_images_browse_b = self.main_window.file_transfer_input_images_browse_button  # type: QtWidgets.QPushButton
        self.failed_rename_browse_b = self.main_window.file_transfer_failed_rename_images_browse_button  # type: QtWidgets.QPushButton
        self.local_output_browse_b = self.main_window.file_transfer_local_output_browse_button  # type: QtWidgets.QPushButton
        self.network_transfer_browse_b = self.main_window.file_transfer_network_transfer_browse_button  # type: QtWidgets.QPushButton

        self.transfer_time_te = self.main_window.file_transfer_transfer_time_edit  # type: QtWidgets.QTimeEdit

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

    def __connect_signals_to_slots(self):
        pass
