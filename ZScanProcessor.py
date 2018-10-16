#####################################
# Imports
#####################################
# Python native imports
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import signal
import logging
import qdarkstyle

# Load UI
from Resources.UI.ZScanUI import Ui_MainWindow as ZScanUI

# Custom Imports
from Interface.InterfaceCore import Interface

from Framework.TrayNotifier import TrayNotifierCore
from Framework.Settings import SettingsCore
from Framework.Logging import LoggingCore
from Framework.Logging.LiveLogs import LiveLogsCore

from Framework.PreviewProcessor import PreviewProcessorCore
from Framework.ScheduledProcessing import ScheduledProcessingCore


#####################################
# Global Variables
#####################################
UI_LOGO = "logo_small.jpg"


#####################################
# ApplicationWindow Class Definition
#####################################
class ZScanWindow(QtWidgets.QMainWindow, ZScanUI):
    exit_requested_signal = QtCore.pyqtSignal()

    kill_threads_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(ZScanWindow, self).__init__(parent)

        self.setupUi(self)

        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.exit_requested_signal.emit)

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                self.hide()
                event.ignore()


#####################################
# GroundStation Class Definition
#####################################
class ZScanCore(QtCore.QObject):
    exit_requested_signal = QtCore.pyqtSignal()

    start_threads_signal = QtCore.pyqtSignal()
    connect_signals_and_slots_signal = QtCore.pyqtSignal()
    kill_threads_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None,):
        # noinspection PyArgumentList
        super(ZScanCore, self).__init__(parent)

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        self.shared_objects = {
            "core_signals": {
                "start": self.start_threads_signal,
                "kill": self.kill_threads_signal,
                "connect_signals_and_slots": self.connect_signals_and_slots_signal
            },

            "screens": {},
            "regular_classes": {},
            "threaded_classes": {}
        }

        # ###### Instantiate Left And Right Screens ######
        self.shared_objects["screens"]["main_screen"] = \
            self.create_application_window(ZScanWindow, "Zebrafish Scan Processor", (1536, 1024))

        # ##### Instantiate Regular Classes ######
        self.__add_non_thread("Settings", SettingsCore.Settings())
        # QtCore.QSettings().clear()  # Only used to reset when testing defaults on "fresh install"
        # QtGui.QGuiApplication.exit()
        self.__add_non_thread("Logger", LoggingCore.Logger(console_output=False))
        self.__add_non_thread("Tray Notifier", TrayNotifierCore.TrayNotifier(self.shared_objects))
        self.__add_non_thread("Interface", Interface(self.shared_objects))

        # ##### Instantiate Threaded Classes ######
        self.__add_thread("Live Logs", LiveLogsCore.LiveLogs(self.shared_objects))
        self.__add_thread("Preview Processor", PreviewProcessorCore.PreviewProcessor(self.shared_objects))
        self.__add_thread("Schedule Processor", ScheduledProcessingCore.ScheduleProcessor(self.shared_objects))

        self.connect_signals_and_slots_signal.emit()
        self.__connect_signals_to_slots()
        self.start_threads_signal.emit()

    def __add_non_thread(self, name, instance):
        self.shared_objects["regular_classes"][name] = instance

    def __add_thread(self, thread_name, instance):
        self.shared_objects["threaded_classes"][thread_name] = instance

    def __connect_signals_to_slots(self):
        self.shared_objects["screens"]["main_screen"].exit_requested_signal.connect(self.on_exit_requested__slot)

    def on_exit_requested__slot(self):
        self.kill_threads_signal.emit()

        # Wait for Threads
        for thread in self.shared_objects["threaded_classes"]:
            self.shared_objects["threaded_classes"][thread].wait()

        QtGui.QGuiApplication.exit()

    @staticmethod
    def create_application_window(ui_class, title, size):
        app_window = ui_class()  # Make a window in this application
        app_window.setWindowTitle(title)  # Sets the window title

        app_window.show()  # Shows the window in full screen mode

        return app_window


#####################################
# Main Definition
#####################################
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # This allows the keyboard interrupt kill to work properly

    # ########## Start the QApplication Framework ##########
    application = QtWidgets.QApplication(sys.argv)  # Create the ase qt gui application
    application.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    app_icon = QtGui.QIcon()
    app_icon.addFile(UI_LOGO, QtCore.QSize(16, 16))
    app_icon.addFile(UI_LOGO, QtCore.QSize(24, 24))
    app_icon.addFile(UI_LOGO, QtCore.QSize(32, 32))
    app_icon.addFile(UI_LOGO, QtCore.QSize(48, 48))
    app_icon.addFile(UI_LOGO, QtCore.QSize(256, 256))
    application.setWindowIcon(app_icon)

    # ########## Set Organization Details for QSettings ##########
    QtCore.QCoreApplication.setOrganizationName("SARL")
    QtCore.QCoreApplication.setOrganizationDomain("http://tanguaylab.com")
    QtCore.QCoreApplication.setApplicationName("ZScanProcessor")

    # ########## Start Ground Station If Ready ##########
    ground_station = ZScanCore()
    application.exec_()  # Execute launching of the application