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
    def __init__(self):
        super(Settings, self).__init__()

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
        self.settings.setValue("file_and_transfer_settings/appdata_directory", full_path)
