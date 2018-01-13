"""
    This file contains the barcode detection worker class
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
from PyQt5 import QtCore, QtWidgets, QtGui
import logging
import subprocess
import cv2
import qimage2ndarray
from os.path import exists, isdir
from os import mkdir, remove, makedirs
import glob
from PIL import Image
import zbar

# Custom Import
from Framework import WorkerCore

#####################################
# Global Variables
#####################################
# Settings for imports


#####################################
# Detection Preview Class Definition
#####################################
class BarcodeDetectorWorker(QtCore.QThread):
    preview_images_ready_signal = QtCore.pyqtSignal()

    def __init__(self, image_to_detect):
        super(BarcodeDetectorWorker, self).__init__()

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########

    def run(self):
        while self.run_thread_flag:

            self.msleep(100)

    # noinspection PyUnresolvedReferences
    def connect_signals_to_slots__slot(self):
        pass