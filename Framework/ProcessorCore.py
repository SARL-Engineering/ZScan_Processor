"""
    This file contains the processor core sub-class
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
from PyQt5 import QtCore, QtWidgets
import logging


#####################################
# Processor Core Class Definition
#####################################
class ProcessorCore(QtCore.QThread):
    def __init__(self, main_window):
        super(ProcessorCore, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window  # type: QtWidgets.QMainWindow

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## Class Variables ##########

        # ########## Load class settings ##########
        self.__load_settings()

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

        # ########## Start Thread ##########
        self.start()

    def run(self):
        self.logger.debug("Processor Core Thread Starting...")
        while self.run_thread_flag:
            self.msleep(100)

        self.logger.debug("Processor Core Thread Stopping...")

    def __load_settings(self):
        pass

    # noinspection PyUnresolvedReferences
    def __connect_signals_to_slots(self):
        self.main_window.kill_threads_signal.connect(self.on_kill_threads__slot)

    def on_kill_threads__slot(self):
        self.run_thread_flag = False


