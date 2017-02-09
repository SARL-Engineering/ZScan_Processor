"""
    This file contains the Settings sub-class as part of the Framework Class
    This class handles initialization of system settings and handling defaults when no settings are found
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
from PyQt5 import QtCore
import os

# Custom imports

#####################################
# Global Variables
#####################################


#####################################
# PickAndPlateLogger Definition
#####################################
class Settings(QtCore.QObject):
    def __init__(self, main_window):
        super(Settings, self).__init__()

        # ########## Reference to highest level window ##########
        self.main_window = main_window  # type: QtWidgets.QMainWindow

        # ########## Set up settings for program ##########
        self.__setup_settings()

        # ########## Create Instance of settings ##########
        self.settings = QtCore.QSettings()

        # ########## Create Instance of settings ##########
        self.__set_hardcoded_settings()

    @staticmethod
    def __setup_settings():
        # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
        QtCore.QCoreApplication.setOrganizationName("OSU SARL")
        # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
        QtCore.QCoreApplication.setOrganizationDomain("http://tanguaylab.com/")
        # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
        QtCore.QCoreApplication.setApplicationName("ZScanProcessor")

    def __set_hardcoded_settings(self):
        # Set the temporary directory used to store files while processing them
        app_data_dir = os.environ["APPDATA"]
        folder_name = "ZScanProcessor"
        full_path = app_data_dir + "\\" + folder_name
        self.settings.setValue("file_transfer_and_settings/appdata_directory", full_path)
