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
