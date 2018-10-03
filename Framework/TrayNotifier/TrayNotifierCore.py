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
UI_LOGO = "Resources/UI/logo_small.jpg"


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
        self.system_tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(UI_LOGO))
        self.system_tray_menu = QtWidgets.QMenu()
        self.system_tray_menu.addAction("Show")
        self.system_tray_menu.addAction("Exit")

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

    def show_informational_message(self, message, time=2000):
        self.system_tray_icon.showMessage("Zebrafish Scan Processor", message, QtWidgets.QSystemTrayIcon.Information,
                                          time)

    def show_failure_message(self, message, time=10000):
        self.system_tray_icon.showMessage("Zebrafish Scan Processor", message, QtWidgets.QSystemTrayIcon.Critical,
                                          time)

    def on_tray_menu_item_clicked(self, event):
        if event == QtWidgets.QSystemTrayIcon.Context:  # Happens on right-click, ignore for tray menu instead
            pass
        elif event == QtWidgets.QSystemTrayIcon.Trigger:
            self.main_screen.show()
        elif event.text() == "Show":
            self.main_screen.show()
        elif event.text() == "Exit":
            self.system_tray_icon.hide()
            self.main_screen.exit_requested_signal.emit()

    def on_kill_threads__slot(self):
        pass

    def setup_signals(self):
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)

        self.system_tray_icon.activated.connect(self.on_tray_menu_item_clicked)
        self.system_tray_menu.triggered.connect(self.on_tray_menu_item_clicked)

