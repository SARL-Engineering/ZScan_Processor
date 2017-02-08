"""
    This file contains the live logs page sub-class
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
# Live Logs Class Definition
#####################################
class LiveLogs(QtCore.QThread):

    thread_stopping_signal = QtCore.pyqtSignal()

    def __init__(self, main_window):
        super(LiveLogs, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True

        # ########## References to GUI Elements ##########
        self.live_log_info_b = self.main_window.live_log_info_checkbox
        self.live_log_warning_b = self.main_window.live_log_warning_checkbox
        self.live_log_error_b = self.main_window.live_log_error_checkbox
        self.live_log_debug_b = self.main_window.live_log_debug_checkbox
        self.live_log_tb = self.main_window.live_log_text_browser

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

        # ########## Start Thread ##########
        self.start()

    def run(self):
        self.logger.debug("Live Logs Thread Starting...")
        while self.run_thread_flag:
            if False:
                pass
            else:
                self.msleep(250)

        self.logger.debug("Live Logs Thread Exiting...")
        self.thread_stopping_signal.emit()

    # noinspection PyUnresolvedReferences
    def __connect_signals_to_slots(self):
        self.main_window.kill_threads_signal.connect(self.on_kill_threads__slot)

    def on_kill_threads__slot(self):
        self.run_thread_flag = False
