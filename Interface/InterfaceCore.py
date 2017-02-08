"""
    This file contains the interface core sub-class
    This instantiates all the high level sub-classes for the interface
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

# Custom imports
from Interface.LiveLogs.LiveLogsCore import LiveLogs
from Interface.DetectionSettings.DetectionSettingsCore import DetectionSettings
from Interface.FileAndTransferSettings.FileAndTransferSettingsCore import FileAndTransferSettings
from Interface.About.AboutCore import About


#####################################
# Interface Class Definition
#####################################
class Interface(QtCore.QObject):
    def __init__(self, main_window):
        super(Interface, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Instantiations of sub-classes ##########
        self.live_logs_class = LiveLogs(self.main_window)
        self.detection_class = DetectionSettings(self.main_window)
        self.file_transfer_and_settings_class = FileAndTransferSettings(self.main_window)
        self.about_class = About(self.main_window)

        # ########## References to GUI Elements ##########
        self.tab_widget = self.main_window.tab_widget  # type: QtWidgets.QTabWidget

        # ########## Set default interface parameters ##########
        # Always open to first tab on launch
        self.tab_widget.setCurrentIndex(0)
