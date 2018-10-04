#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore
import logging
import cv2

from pyzbar import pyzbar

#####################################
# Global Variables
#####################################


#####################################
# DetectionProcessor Definition
#####################################
class DetectionWorker(QtCore.QThread):

    def __init__(self, image, x, x_size, y, y_size, threshold):
        super(DetectionWorker, self).__init__()

        self.image = image.copy()
        self.x = x
        self.x_size = x_size
        self.y = y
        self.y_size = y_size
        self.threshold = threshold

        # ########## Get the settings instance ##########
        self.settings = QtCore.QSettings()

        # ########## Get the instance of the logger ##########
        self.logger = logging.getLogger("zscanprocessor")

        # ########## Class variables ##########
        self.original_image = None
        self.threshold_image = None
        self.barcode_value = None

    def run(self):
        try:
            height, width, _ = self.image.shape

            x_max = min((self.x + self.x_size), width)
            y_max = min((self.y + self.y_size), height)

            self.original_image = self.image[self.y:y_max, self.x:x_max]
            cropped_gray = cv2.cvtColor(self.original_image, cv2.COLOR_RGB2GRAY)
            ret, threshold_barcode = cv2.threshold(cropped_gray, self.threshold, 255, cv2.THRESH_BINARY)
            self.threshold_image = cv2.cvtColor(threshold_barcode, cv2.COLOR_GRAY2RGB)

            barcodes = pyzbar.decode(self.threshold_image)

            if barcodes:
                self.original_image = cv2.rotate(self.original_image, 0)
                self.threshold_image = cv2.rotate(self.threshold_image, 0)
                self.barcode_value = barcodes[0].data.decode("utf-8")

        except Exception as e:
            print(e)


