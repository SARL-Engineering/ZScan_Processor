# Zebrafish Scan Processor
###### [Download Latest Release](https://github.com/SARL-Engineering/ZScan_Processor/releases/latest)
## Main Purpose
This application processes high-resolution scanned images of 96-well scientific plates by doing the following:
1. Monitors an input scans folder and automatically begins processing once the scan is complete.
2. Splits the image into the two individual plates.
3. Automatically detects the barcode on each plate to name the outputs automatically.
4. Splits and names each well based on the scan creation datetime, plate number, and well location.
5. Saves a compressed version of the individual plate image.
6. MySQL INSERT/UPDATE allows for quick auditing of processed plates from a central database.
7. At a designated time, transfers all processed plates to a network share/designated transfer folder.

### Other Features
* Overlays the detected barcode onto all processed images for easy sanity checking when analyzing images.
* Minimizes to tray area for unobtrusive background processing.
* Provides system notifications when plates are processed/fail.
* Maintains logs of all detections, transfers, and failures.
* Includes built-in calibration interface for easy adjustment to scanner and plate differences.
* Allows for a custom MySQL query string for easy adaptation to different database layouts.
* Saves full-resolution backups of failed plates to ensure data is not lost.

##### Special Note
The database section of this program does NOT hash the password. It is stored in plaintext in the registry.
Please keep this in mind when creating a MySQL user for this application.

## Screenshots
### Processed Outputs
#### Full Plate & Well
<img src="_screenshots_/plate_example.jpg" height="400" title="plate_example"><img src="_screenshots_/well_example.jpg" height="400" title="well_example">

#### Folder Structure & Explorer Preview
<img src="_screenshots_/folder_structure.jpg" height="400" title="folder_structure"><img src="_screenshots_/output.jpg" height="400" title="explorer_example">

### Application
### Logs Screen
<img src="_screenshots_/logs.jpg" title="logs_screen">

### Settings - Plate Splitting
<img src="_screenshots_/settings_plate_splitting.jpg" title="plate_splitting_screen">

### Settings - Plate Top
<img src="_screenshots_/settings_top_plate.jpg" title="plate_top_screen">

### Settings - Plate Bottom
<img src="_screenshots_/settings_bottom_plate.jpg" title="plate_bottom_screen">

### Settings - Files and Transfers
<img src="_screenshots_/settings_files_and_transfers.jpg" title="files_and_transfers_screen">

### Settings - Database
<img src="_screenshots_/settings_database.jpg" title="database_screen">

### System Notifications
<img src="_screenshots_/system_notification.jpg" title="system_notifications_window">

### Tray Icon
<img src="_screenshots_/tray_icon.jpg" title="tray_icon_location">

### Example Database Output
<img src="_screenshots_/database_output.jpg" title="database_output_example">

## Build Information
* Python 3.7 64-bit
    * PyQt5
    * pyzbar
    * opencv
    * pillow
    * mysql-connector
    * numpy
    * qdarkstyle
    * qimage2ndarray
* Executable built with pyinstaller
* Installer built with NSIS
