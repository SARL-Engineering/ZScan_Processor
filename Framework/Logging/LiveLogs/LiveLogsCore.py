#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore, QtWidgets, QtGui
import logging
import os


#####################################
# Live Logs Class Definition
#####################################
class LiveLogs(QtCore.QThread):

    text_ready_signal = QtCore.pyqtSignal()

    def __init__(self, shared_objects):
        super(LiveLogs, self).__init__()

        # ########## Reference to top level window ##########
        self.shared_objects = shared_objects
        self.core_signals = self.shared_objects["core_signals"]
        self.main_screen = self.shared_objects["screens"]["main_screen"]  # type: ZScanUI

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Thread Flags ##########
        self.run_thread_flag = True
        self.open_log_file_flag = True
        self.show_log_file_flag = True

        # ########## References to GUI Elements ##########
        self.live_log_info_cb = self.main_screen.live_log_info_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_warning_cb = self.main_screen.live_log_warning_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_error_cb = self.main_screen.live_log_error_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_debug_cb = self.main_screen.live_log_debug_checkbox  # type: QtWidgets.QCheckBox
        self.live_log_tb = self.main_screen.live_log_text_browser  # type: QtWidgets.QTextBrowser

        # ########## Class Variables ##########
        self.log_file_path = None
        self.log_file_reader = None
        self.log_file_prev_size = 0
        self.log_browser_string = ""

        self.checkboxes_changed = False

        # ########## Load class settings ##########
        self.__load_settings()

        # ########## Setup program start signal connections ##########
        self.setup_signals()

    def run(self):
        self.logger.debug("Live Logs Thread Starting...")

        while self.run_thread_flag:
            if self.open_log_file_flag:
                self.__open_log_file()
                self.open_log_file_flag = False
            elif self.show_log_file_flag:
                self.__show_updated_log_file()
                self.msleep(10)

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

        # This keeps the text box from being scrollable
        self.live_log_tb.verticalScrollBar().blockSignals(True)

    # noinspection PyUnresolvedReferences
    def connect_signals_and_slots(self):
        self.text_ready_signal.connect(self.__on_text_should_update_signal__slot)
        self.live_log_tb.textChanged.connect(self.__on_move_cursor_needed__slot)

        self.live_log_info_cb.toggled.connect(self.__on_checkbox_changed__slot)
        self.live_log_warning_cb.toggled.connect(self.__on_checkbox_changed__slot)
        self.live_log_error_cb.toggled.connect(self.__on_checkbox_changed__slot)
        self.live_log_debug_cb.toggled.connect(self.__on_checkbox_changed__slot)

        self.main_screen.kill_threads_signal.connect(self.on_kill_threads__slot)

    def __open_log_file(self):
        # Get the log file path
        appdata_base_directory = self.settings.value("file_and_transfer_settings/appdata_directory", type=str)
        log_directory = appdata_base_directory + "\\logs"
        self.log_file_path = log_directory + "\\log.txt"

        # Open the class' reader for the file
        self.log_file_reader = open(self.log_file_path, 'r')

    def __show_updated_log_file(self):
        # Go to end of file so we can get its size
        self.log_file_reader.seek(0, os.SEEK_END)
        log_file_size = self.log_file_reader.tell()

        if log_file_size != self.log_file_prev_size or self.checkboxes_changed:
            self.log_browser_string = ""

            # Seek back to the beginning of the file and read in the lines
            # Also strip it down to the most recent 100
            self.log_file_reader.seek(0)
            log_lines = self.log_file_reader.readlines()[-300:]

            # Go through line by line and only add lines that are selected to be shown via the checkboxes
            for line in reversed(log_lines):
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

            self.log_file_prev_size = log_file_size
            self.checkboxes_changed = False

    def __on_text_should_update_signal__slot(self):
        self.live_log_tb.clear()
        self.live_log_tb.append(self.log_browser_string)

    def __on_move_cursor_needed__slot(self):
        # Move the cursor to the end when the text browser text updates. This essentially scrolls constantly.
        self.live_log_tb.moveCursor(QtGui.QTextCursor.End)

    def __on_checkbox_changed__slot(self):
        self.settings.setValue("live_logs_settings/info_checkbox_state", int(self.live_log_info_cb.isChecked()))
        self.settings.setValue("live_logs_settings/warning_checkbox_state", int(self.live_log_warning_cb.isChecked()))
        self.settings.setValue("live_logs_settings/error_checkbox_state", int(self.live_log_error_cb.isChecked()))
        self.settings.setValue("live_logs_settings/debug_checkbox_state", int(self.live_log_debug_cb.isChecked()))

        self.checkboxes_changed = True

    def on_kill_threads__slot(self):
        self.run_thread_flag = False

    def setup_signals(self):
        self.core_signals["start"].connect(self.start)
        self.core_signals["kill"].connect(self.on_kill_threads__slot)
        self.core_signals["connect_signals_and_slots"].connect(self.connect_signals_and_slots)
