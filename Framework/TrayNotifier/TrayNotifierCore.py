# coding=utf-8
#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging

#####################################
# Global Variables
#####################################


#####################################
# TrayNotifier Class Definition
#####################################
class TrayNotifier(QtCore.QObject):
    def __init__(self, shared_objects):
        super(TrayNotifier, self).__init__()

        # ########## Reference to objects and main screen objects ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]

        # ########## Get the settings and logging instances ##########
        self.settings = QtCore.QSettings()
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Class Variables ##########
        self.system_tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("Resources/UI/logo_small.jpg"))
        self.system_tray_menu = QtWidgets.QMenu()

        # ########## Setup tray icon ##########
        self.setup_tray_icon()

        # ########## Setup program start signal connections ##########
        self.setup_signals()

    def setup_tray_icon(self):
        self.system_tray_icon.setContextMenu(self.system_tray_menu)
        self.system_tray_icon.show()
        self.system_tray_icon.showMessage("Zebrafish Scan Processor", "Application started.\nUpdates will be " +
                                          "shown here.", QtWidgets.QSystemTrayIcon.Information, 5000)

    def connect_signals_and_slots(self):
        pass

    def on_kill_threads__slot(self):
        self.system_tray_icon.hide()

    def setup_signals(self):
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)

