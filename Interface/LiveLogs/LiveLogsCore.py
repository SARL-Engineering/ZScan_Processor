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
from PyQt5 import QtCore, QtWidgets, QtGui
import logging


#####################################
# Live Logs Class Definition
#####################################
class LiveLogs(QtCore.QThread):

    text_ready_signal = QtCore.pyqtSignal()

    def __init__(self, main_window):
        super(LiveLogs, self).__init__()

        # ########## Reference to top level window ##########
        self.main_window = main_window  # type: QtWidgets.QMainWindow

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True
        self.open_log_file_flag = True
        self.show_log_file_flag = True

        # ########## References to GUI Elements ##########
        self.live_log_info_cb = self.main_window.live_log_info_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_warning_cb = self.main_window.live_log_warning_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_error_cb = self.main_window.live_log_error_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_debug_cb = self.main_window.live_log_debug_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_tb = self.main_window.live_log_text_browser  # type: QtWidgets.QTextBrowser

        # ########## Class Variables ##########
        self.log_file_path = None
        self.log_file_reader = None
        self.log_file_prev_mtime = 0
        self.log_browser_string = ""

        # ########## Load class settings ##########
        self.__load_settings()

        # ########## Make signal/slot connections ##########
        self.__connect_signals_to_slots()

        # ########## Start Thread ##########
        self.start()

    def run(self):
        self.logger.debug("Live Logs Thread Starting...")

        while self.run_thread_flag:
            if self.open_log_file_flag:
                self.__open_log_file()
                self.open_log_file_flag = False
            elif self.show_log_file_flag:
                self.__show_updated_log_file()
                self.msleep(250)

        self.logger.debug("Live Logs Thread Stopping...")

    def __load_settings(self):
        live_log_info_cb_state = self.settings.value("live_logs_settings/info_checkbox_state", 1, type=int)
        live_log_warning_cb_state = self.settings.value("live_logs_settings/warning_checkbox_state", 1, type=int)
        live_log_error_cb_state = self.settings.value("live_logs_settings/error_checkbox_state", 1, type=int)
        live_log_debug_cb_state = self.settings.value("live_logs_settings/debug_checkbox_state", 0, type=int)

        self.live_log_info_cb.setChecked(live_log_info_cb_state)
        self.live_log_warning_cb.setChecked(live_log_warning_cb_state)
        self.live_log_error_cb.setChecked(live_log_error_cb_state)
        self.live_log_debug_cb.setChecked(live_log_debug_cb_state)

    # noinspection PyUnresolvedReferences
    def __connect_signals_to_slots(self):
        self.text_ready_signal.connect(self.__on_text_should_update_signal__slot)
        self.live_log_tb.textChanged.connect(self.__on_move_cursor_needed__slot)

        self.live_log_info_cb.toggled.connect(self.__on_checkbox_changed__slot)
        self.live_log_warning_cb.toggled.connect(self.__on_checkbox_changed__slot)
        self.live_log_error_cb.toggled.connect(self.__on_checkbox_changed__slot)
        self.live_log_debug_cb.toggled.connect(self.__on_checkbox_changed__slot)

        self.main_window.kill_threads_signal.connect(self.on_kill_threads__slot)

    def __open_log_file(self):
        # Get the log file path
        appdata_base_directory = self.settings.value("file_transfer_and_settings/appdata_directory", type=str)
        log_directory = appdata_base_directory + "\\logs"
        self.log_file_path = log_directory + "\\log.txt"

        # Open the class' reader for the file
        self.log_file_reader = open(self.log_file_path, 'r')

    def __show_updated_log_file(self):
        self.log_browser_string = ""

        # Seek back to the beginning of the file and read in the lines
        self.log_file_reader.seek(0)
        log_lines = self.log_file_reader.readlines()

        # Go through line by line and only add lines that are selected to be shown via the checkboxes
        for line in log_lines:
            log_line_type = line.split(" ")[0]

            if log_line_type == "INFO":
                if self.live_log_info_cb.isChecked():
                    self.log_browser_string += line
            elif log_line_type == "WARNING":
                if self.live_log_warning_cb.isChecked():
                    self.log_browser_string += line
            elif log_line_type == "ERROR":
                if self.live_log_error_cb.isChecked():
                    self.log_browser_string += line
            elif log_line_type == "DEBUG":
                if self.live_log_debug_cb.isChecked():
                    self.log_browser_string += line
            else:
                self.log_browser_string += line

        # Display the text
        self.text_ready_signal.emit()

    def __on_text_should_update_signal__slot(self):
        self.live_log_tb.setText(self.log_browser_string)

    def __on_move_cursor_needed__slot(self):
        # Move the cursor to the end when the text browser text updates. This essentially scrolls constantly.
        self.live_log_tb.moveCursor(QtGui.QTextCursor.End)

    def __on_checkbox_changed__slot(self):
        self.settings.setValue("live_logs_settings/info_checkbox_state", int(self.live_log_info_cb.isChecked()))
        self.settings.setValue("live_logs_settings/warning_checkbox_state", int(self.live_log_warning_cb.isChecked()))
        self.settings.setValue("live_logs_settings/error_checkbox_state", int(self.live_log_error_cb.isChecked()))
        self.settings.setValue("live_logs_settings/debug_checkbox_state", int(self.live_log_debug_cb.isChecked()))

    def on_kill_threads__slot(self):
        self.run_thread_flag = False
