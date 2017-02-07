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
# along with "Pick And Plate".  If not, see <http://www.gnu.org/licenses/>.

#####################################
# Imports
#####################################
# Python native imports
import sys
from PyQt5 import QtWidgets, uic
import signal


#####################################
# Global Variables
#####################################
UI_FILE_PATH = "Interface/ZScanUI.ui"


#####################################
# Application Class Definition
#####################################
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)

        # ########## Set up QT Application Window ##########
        self.show()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # This allows the keyboard interrupt kill to work  properly
    app = QtWidgets.QApplication(sys.argv)  # Create the base qt gui application
    app_window = ApplicationWindow()  # Make a window in this application using the pnp MyWindowClass
    app_window.show()  # Show the window in the application
    app.exec_()  # Execute launching of the application
