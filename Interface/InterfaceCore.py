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
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI

from Interface.About import AboutCore
from Interface.Settings import FileAndTransferSettingsCore
from Interface.Settings import DetectionSettingsCore


#####################################
# Interface Class Definition
#####################################
class Interface(QtCore.QObject):
    def __init__(self, shared_objects):
        super(Interface, self).__init__()

        # ########## Reference to objects and main screen objects ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## Instantiations of sub-classes ##########
        self.detection_settings = DetectionSettingsCore.DetectionSettings(self.shared_objects)
        self.file_transfer_and_settings_class = FileAndTransferSettingsCore.FileAndTransferSettings(self.shared_objects)
        self.about_class = AboutCore.About(self.shared_objects)

        # ########## References to GUI Elements ##########
        self.main_tab_widget = self.main_screen.main_tab_widget  # type: QtWidgets.QTabWidget
        self.settings_tab_widget = self.main_screen.settings_tab_widget  # type: QtWidgets.QTabWidget

        # ########## Set default interface parameters ##########
        # Always open to first tab on launch
        self.main_tab_widget.setCurrentIndex(0)
        self.settings_tab_widget.setCurrentIndex(0)

        self.setup_signals()

    def connect_signals_and_slots(self):
        pass

    def setup_signals(self):
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)
