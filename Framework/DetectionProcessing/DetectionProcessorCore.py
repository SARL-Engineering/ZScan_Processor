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
from PyQt5 import QtCore
import logging

# Custom imports
from Framework.DetectionProcessing import DetectionWorkerCore

#####################################
# Global Variables
#####################################
SCAN_STEP_SIZE_X = 100
SCAN_STEP_SIZE_Y = 250


#####################################
# DetectionProcessor Definition
#####################################
class DetectionProcessor(QtCore.QObject):
    start_workers__signal = QtCore.pyqtSignal()

    def __init__(self, processing_dictionary):
        super(DetectionProcessor, self).__init__()

        self.processing_dictionary = processing_dictionary

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Class Variables ##########
        self.scan_box_image = None
        self.workers = []

        self.original_image = None
        self.threshold_image = None
        self.barcode_value = None
        self.threshold_value = None

        # ########## Setup workers ##########
        self.setup_workers()

    def setup_workers(self):
        self.scan_box_image = self.processing_dictionary["scan_box_image"]
        barcode_x_size = self.processing_dictionary["barcode_x_size"]
        barcode_y_size = self.processing_dictionary["barcode_y_size"]
        threshold_center = self.processing_dictionary["threshold_center"]
        threshold_range = self.processing_dictionary["threshold_range"]

        threshold_min = max(threshold_center - threshold_range, 0)
        threshold_max = max(threshold_center + threshold_range, 0)

        height, width, _ = self.scan_box_image.shape

        x_max = max(width - barcode_x_size, 0)
        y_max = max(height - barcode_y_size, 0)

        for x in range(0, x_max, SCAN_STEP_SIZE_X):
            for y in range(0, y_max, SCAN_STEP_SIZE_Y):
                for threshold in range(threshold_min, threshold_max):
                    worker = DetectionWorkerCore.DetectionWorker(self.scan_box_image, x, barcode_x_size, y,
                                                                 barcode_y_size, threshold)
                    self.start_workers__signal.connect(worker.start)
                    self.workers.append(worker)

    def process(self):
        self.start_workers__signal.emit()

        done_waiting_for_workers = False
        found_index = None

        # Check all workers, wait for all to finish, or for index to be found
        while not done_waiting_for_workers:
            workers_left_alive = False
            for index, worker in enumerate(self.workers):
                if worker.isRunning():
                    workers_left_alive = True

                if worker.barcode_value:
                    found_index = index
                    done_waiting_for_workers = True

            if not workers_left_alive:
                done_waiting_for_workers = True

        # If found, terminate all running threads, then store valid data
        if found_index:
            self.original_image = self.workers[found_index].original_image.copy()
            self.threshold_image = self.workers[found_index].threshold_image.copy()
            self.barcode_value = str(self.workers[found_index].barcode_value)
            self.threshold_value = str(self.workers[found_index].threshold)

    def bardcode_found(self):
        return self.barcode_value is not None

    def get_barcode_data(self):
        return {
            "original_image": self.original_image,
            "threshold_image": self.threshold_image,
            "threshold_value": self.threshold_value,
            "barcode_value": self.barcode_value
        }

    def cleanup(self):
        for worker in self.workers:
            worker.wait()

        for _ in range(len(self.workers)):
            del self.workers[0]
