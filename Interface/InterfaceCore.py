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
from Interface.Settings import DatabaseSettingsCore


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
        self.database_settings = DatabaseSettingsCore.DatabaseSettings(self.shared_objects)
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
