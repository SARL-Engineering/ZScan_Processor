#####################################
# Imports
#####################################
# Python native imports
from PyQt5 import QtCore
import subprocess
import logging
import cv2
from PIL import Image

#####################################
# Global Variables
#####################################
NO_PLATE_MEAN_THRESHOLD = 235
UI_PREVIEW_BC_WIDTH = 450
UI_PREVIEW_BC_HEIGHT = 45

BARCODE_NUM_DIGITS = 9


#####################################
# Detection Worker Class Definition
#####################################
# This one is primarily used by DetectionPreview
class DetectionWorker(QtCore.QThread):

    barcode_found_signal = QtCore.pyqtSignal()

    def __init__(self, parent, y1, y2, x1, x2, threshold, cv2_image, image_base_path, zbar_path):
        super(DetectionWorker, self).__init__()

        self.detect_parent = parent

        self.y1 = y1
        self.y2 = y2
        self.x1 = x1
        self.x2 = x2

        self.threshold = threshold
        self.cv2_image = cv2_image

        self.image_base_path = image_base_path
        self.zbar_path = zbar_path

        self.result = "Not Found"
        self.cv2_raw = None
        self.cv2_threshold = None

        self.barcode_found_signal.connect(self.detect_parent.on_barcode_found__slot)

        self.run()

    def run(self):
        self.cv2_raw = self.cv2_image[self.y1:self.y2, self.x1:self.x2]
        cv2_barcode_gray = cv2.cvtColor(self.cv2_raw, cv2.COLOR_BGR2GRAY)
        ret, self.cv2_threshold = cv2.threshold(cv2_barcode_gray, self.threshold, 255, cv2.THRESH_BINARY)

        full_path = self.image_base_path + "\\" + str(self.threshold) + "__" + str(self.y1) + "_" + str(self.y2) + "_" + str(self.x1) + "_" + str(self.x2) + ".png"

        cv2.imwrite(full_path, self.cv2_threshold)

        process = subprocess.Popen([self.zbar_path, "--raw", "-q", full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        out = out.decode("utf-8").strip('\n')

        is_no_plate = cv2.mean(cv2_barcode_gray)[0] > NO_PLATE_MEAN_THRESHOLD



        if out != "" or is_no_plate:
            if self.is_number(out) and len(out) == BARCODE_NUM_DIGITS:
                self.result = out
                self.barcode_found_signal.emit()
            else:
                self.result = "No Plate Present"

            resized_raw = cv2.resize(self.cv2_raw, (UI_PREVIEW_BC_WIDTH, UI_PREVIEW_BC_HEIGHT))
            self.cv2_raw = cv2.cvtColor(resized_raw, cv2.COLOR_BGR2RGB)

            resized_threshold = cv2.resize(self.cv2_threshold, (UI_PREVIEW_BC_WIDTH, UI_PREVIEW_BC_HEIGHT))
            self.cv2_threshold = cv2.cvtColor(resized_threshold, cv2.COLOR_GRAY2RGB)

    @staticmethod
    def is_number(input_string):
        try:
            float(input_string)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(input_string)
            return True
        except (TypeError, ValueError):
            pass

        return False


#####################################
# Detection Worker Class Definition
#####################################
# This one is primarily used by DetectionPreview
class CoreImageSplitWorker(QtCore.QThread):
    def __init__(self, parent, image_path, base_output_directory):
        super(CoreImageSplitWorker, self).__init__(parent)

        self.image_path = image_path
        self.base_output_directory = base_output_directory

        # ########## Get the Pick And Plate instance of the logger ##########
        self.logger = logging.getLogger("ZScanProcessor")

    def run(self):
        self.msleep(100)

#  ##### GENERAL PROCESS #####
# Start processing
# Find all raw images
# Split raw images into files eg original_filename_top.png (multi-threaded)
#     # These also needs csv, xml, or in the filename, details about how it was split and where useful areas are
# Wait for splitting to finish
# Move any failed images from failed rename folder for another try
# Go through split images
#     # Detect barcode, move to failed rename folder
#     # Make compressed version of original uncut image, named
#     # Split images into well images, named
# Wait for splitting, naming, moving to finish
# Network transfer files
#     # ABSOLUTELY VERIFY THAT IMAGES ARE TRANSFERRED BEFORE DELETION
#     # If a transfer fails, keep image in local output, try again next time through
