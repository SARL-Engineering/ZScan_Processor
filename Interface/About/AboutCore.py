"""
    This file contains the about page sub-class
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
# About Class Definition
#####################################
class About(QtCore.QObject):
    def __init__(self, shared_objects):
        super(About, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## References to GUI Elements ##########
        self.revision_label = self.main_screen.about_revision_label  # type: QtWidgets.QLabel

        # ########## Set defaults on GUI Elements ##########
        self.__load_settings()

    def __load_settings(self):
        version = self.settings.value("miscellaneous/version", type=str)
        self.revision_label.setText(version)
