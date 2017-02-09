# ZScan_Processor
This application processes scanned images of 96-well plates, splits them, renames them based on the barcode in the image, and transfers the images to a desired location. For more information, please visit the following link: https://www.caperren.com/project/zscan-processor/


# Installation
--Pre-requisites--
ZBar                              (http://zbar.sourceforge.net/)
Python 3.x                        (https://www.python.org/downloads/)
PyQt5                             (https://www.riverbankcomputing.com/software/pyqt/download5)(Pip install is easiest)

Note that I am NOT using python's zbar library. It's at 0.10 and I haven't been able to get it to work, so for now I'm just calling the windows binary. Not ideal, but it works just fine.

# Initial Configuration

1. Run the program and go to the file and transfer settings tab.
2. Enter all the paths. For zbar, it's typically "C:\Program Files (x86)\ZBar\bin\zbarimg.exe"
3. Go to the detection settings tab and click load image.
4. Adjust alignment settings until as desired and the detection previews at the bottom show a valid barcode.
5. Go back to the live logs screen and click minimize to hide the program to the tray.
6. Keep the program running as long as you want it to function.