#!/usr/bin/env python

"""
    Main file used to launch the ZScan Processor
    No other files should be used for launching this application.
"""

__author__ = "Corwin Perren"
__credits__ = [""]
__license__ = "GPL (GNU General Public License) 3.0"
__version__ = "0.1"
__maintainer__ = "Corwin Perren"
__email__ = "caperren@caperren.com"
__status__ = "Development"

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
import sys
from PyQt5 import QtWidgets, QtCore, QtGui, uic
import signal
import ctypes
import logging
import time

# Custom Imports
from Framework.SettingsCore import Settings
from Framework.LoggingCore import Logger
from Interface.InterfaceCore import Interface
from Framework.DetectionPreviewCore import DetectionPreview
from Framework.ProcessorCore import ProcessorCore

#####################################
# Global Variables
#####################################
UI_FILE_PATH = "Resources/UI/ZScanUI.ui"


#####################################
# Application Class Definition
#####################################
class ApplicationWindow(QtWidgets.QMainWindow):

    kill_threads_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        # noinspection PyArgumentList
        super(ApplicationWindow, self).__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)

        # ########## Class Variables ##########
        self.num_threads_running = 0
        self.threads = []

        # ########## Instantiation of program classes ##########
        # Settings class and version number set
        self.settings_class = Settings(self)
        self.settings = QtCore.QSettings()
        self.settings.setValue("miscellaneous/version", __version__)

        # Uncomment these lines to completely reset settings and quit, then re-comment and rerun program
        # self.settings.clear()
        # self.close()

        # Set up the global logger instance
        self.logger_class = Logger(console_output=True)
        self.logger = logging.getLogger("ZScanProcessor")

        # All interface elements
        self.interface_class = Interface(self)

        # The detection preview class for handling calculations and updates to that tab
        self.detection_preview_class = DetectionPreview(self)

        # The processor core class that handles schedules and actually running the program core features
        self.processor_core_class = ProcessorCore(self)

        # ########## Add threads to list for easy access on program close ##########
        self.threads.append(self.interface_class.live_logs_class)
        self.threads.append(self.detection_preview_class)
        self.threads.append(self.processor_core_class)

        # ########## Set up QT Application Window ##########
        self.show()

    def closeEvent(self, event):
        # Tell all threads to die
        self.kill_threads_signal.emit()

        # Wait for all the threads to end properly
        for thread in self.threads:
            thread.wait()

        # Print final log noting shutdown and shutdown the logger to flush to disk
        self.logger.debug("########## Application Stopping ##########")
        logging.shutdown()

        # Accept the close event to properly close the program
        event.accept()


#####################################
# Function Definitions
#####################################
def set_application_icon(app_to_set):
    # Make icon and set it on the passed in object
    icon = QtGui.QIcon()
    icon.addFile("Resources/UI/logo_small.jpg", QtCore.QSize(16, 16))
    icon.addFile("Resources/UI/logo_small.jpg", QtCore.QSize(24, 24))
    icon.addFile("Resources/UI/logo_small.jpg", QtCore.QSize(32, 32))
    icon.addFile("Resources/UI/logo_small.jpg", QtCore.QSize(48, 48))
    icon.addFile("Resources/UI/logo_small.jpg", QtCore.QSize(256, 256))
    app_to_set.setWindowIcon(icon)

    # This tells the OS that python is hosting another program. Doing this makes the icon show up on the task_bar
    my_app_id = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)


#####################################
# Main Definition
#####################################
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # This allows the keyboard interrupt kill to work  properly
    application = QtWidgets.QApplication(sys.argv)  # Create the base qt gui application
    set_application_icon(application)  # Sets the icon
    app_window = ApplicationWindow()  # Make a window in this application using the pnp MyWindowClass
    app_window.setWindowTitle("ZScan Processor")  # Sets the window title
    app_window.show()  # Show the window in the application
    application.exec_()  # Execute launching of the application
