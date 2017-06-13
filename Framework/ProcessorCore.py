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
import datetime
import glob

#####################################
# Global Variables
#####################################
NO_PATH_STRING = "*** No Path Set ***"
IMAGE_EXTENSIONS = ["tif", ".png", ".jpg"]


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
        self.already_ran_today = False
        self.last_day = datetime.datetime.now().day

        self.input_images_path = None
        self.failed_rename_path = None
        self.local_output_path = None
        self.network_transfer_path = None
        self.zbar_path = None
        self.transfer_time_string = None

        self.settings_array = []

        # ########## Load class settings ##########
        self.__load_settings()

    def run(self):
        self.logger.debug("Processor Core Thread Starting...")
        while self.run_thread_flag:
            self.__check_if_day_rollover_reset_needed()

            if self.__time_to_run_and_settings_valid():
                self.__process_images_queue()

            self.msleep(1000)

        self.logger.debug("Processor Core Thread Stopping...")

    def __process_images_queue(self):
        original_image_filenames = self.__get_list_of_original_images_in_path(self.input_images_path)

        if not original_image_filenames:
            self.logger.info("Attempted run, but no original images to process. Waiting for next run...")
            return

        self.logger.info("Found " + str(len(original_image_filenames)) + " original images to process.")

    @staticmethod
    def __get_list_of_original_images_in_path(path):
        image_filenames = []

        for extension in IMAGE_EXTENSIONS:
            image_filenames += glob.glob(path + "\\*" + extension)

        return image_filenames

    def __load_settings(self):
        self.settings_array = []

        self.input_images_path = self.settings.value("file_and_transfer_settings/input_images_path", type=str)
        self.failed_rename_path = self.settings.value("file_and_transfer_settings/failed_rename_path", type=str)
        self.local_output_path = self.settings.value("file_and_transfer_settings/local_output_path", type=str)
        self.network_transfer_path = self.settings.value("file_and_transfer_settings/network_transfer_path", type=str)
        self.zbar_path = self.settings.value("file_and_transfer_settings/zbar_path", type=str)
        self.transfer_time_string = self.settings.value("file_and_transfer_settings/network_transfer_time", type=str)

        self.input_images_path = self.input_images_path.replace("/", "\\")
        self.failed_rename_path = self.failed_rename_path.replace("/", "\\")
        self.local_output_path = self.local_output_path.replace("/", "\\")
        self.network_transfer_path = self.network_transfer_path.replace("/", "\\")

        self.settings_array.append(self.input_images_path)
        self.settings_array.append(self.failed_rename_path)
        self.settings_array.append(self.local_output_path)
        self.settings_array.append(self.network_transfer_path)
        self.settings_array.append(self.zbar_path)

    def __check_if_day_rollover_reset_needed(self):
        current_day = datetime.datetime.now().day

        if current_day > self.last_day:
            self.already_ran_today = False
            self.last_day = current_day

    def __time_to_run_and_settings_valid(self):
        self.__load_settings()

        now, run_time = self.__get_current_time_and_run_time()

        if now.hour == run_time.hour and now.minute == run_time.minute and not self.already_ran_today:
            self.already_ran_today = True

            for setting in self.settings_array:
                if setting == NO_PATH_STRING:
                    self.logger.error("Missing path in file and transfer settings. Please update and try again...")
                    return False

            self.logger.info("Settings valid and start time passed. Attempting to process image queue.")
            return True

    def __get_current_time_and_run_time(self):
        # Checking if run time has passed
        now = datetime.datetime.now()

        run_time = datetime.datetime.strptime(self.transfer_time_string, "%I:%M %p")

        return now, run_time

    # noinspection PyUnresolvedReferences
    def connect_signals_to_slots__slot(self):
        self.main_window.interface_class.file_transfer_and_settings_class.file_and_transfer_settings_changed_signal.connect(
            self.on_file_and_transfer_settings_changed__slot)

        self.main_window.kill_threads_signal.connect(self.on_kill_threads__slot)

    def on_file_and_transfer_settings_changed__slot(self):
        self.already_ran_today = False

    def on_kill_threads__slot(self):
        self.run_thread_flag = False
