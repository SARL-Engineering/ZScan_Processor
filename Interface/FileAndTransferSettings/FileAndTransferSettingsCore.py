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


#####################################
# File and Transfer Class Definition
#####################################
class FileAndTransferSettings(QtCore.QObject):
    def __init__(self, main_window):
        super(FileAndTransferSettings, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## References to GUI Elements ##########
        self.author_label = self.main_window.about_author_label  # type: QtWidgets.QLabel

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

    def __connect_signals_to_slots(self):
        pass
