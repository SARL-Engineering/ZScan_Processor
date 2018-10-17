# Zebrafish Scan Processor
###### [Download Latest Release](https://github.com/SARL-Engineering/ZScan_Processor/releases/latest)
## Main Purpose
This application processes high-resolution scanned images of 96-well scientific plates by doing the following:
1. Monitors an input scans folder and automatically begins processing once the scan is complete.
2. Splits the image into the two individual plates.
3. Automatically detects the barcode on each plate to name the outputs automatically.
4. Splits and names each well based on the scan creation datetime, plate number, and well location.
5. Saves a compressed version of the individual plate image.
6. Writes the plate name to a MySQL database for quick auditing of completed plates.
7. At a designated time, transfers all processed plates to a network share/designated transfer folder.

### Other Features
* Overlays the detected barcode onto all processed images for easy sanity checking when analyzing images.
* Minimizes to tray area for unobtrusive background processing.
* Provides system notifications when plates are processed/fail.
* Maintains logs of all detections, transfers, and failures.
* Includes built-in calibration interface for easy adjustment to scanner and plate differences.
* Allows for a custom MySQL insert string for easy adaptation to different database layouts (may add more features later).
* Saves full-resolution backups of failed plates to ensure data is not lost.

##### Special Note
The database section of this program does NOT hash the password. It is stored in plaintext in the registry.
Please keep this in mind when creating a MySQL user for this application.

## Screenshots
### Processed Outputs
#### Full Plate
![plate_example]

#### Plate Well
![well_example]

#### Explorer Preview
![explorer_preview]

### Folder Structure
![folder_structure]

### Logs Screen
![logs]

### Settings - Plate Splitting
![settings_plate_split]

### Settings - Plate Top
![settings_top]

### Settings - Plate Bottom
![settings_bottom]

### Settings - Files and Transfers
![settings_files_transfers]

### Settings - Database
![settings_database]

### System Notifications
![system_notification]

### Tray Icon
![tray_icon]

### Example Database Output
![database_output]

[logs]:_screenshots_/logs.png
[plate_example]:_screenshots_/plate_example.png
[well_example]:_screenshots_/well_example.png
[explorer_preview]:_screenshots_/output.png
[folder_structure]:_screenshots_/folder_structure.png
[settings_bottom]:_screenshots_/settings_bottom_plate.png
[settings_top]:_screenshots_/settings_top_plate.png
[settings_plate_split]:_screenshots_/settings_plate_splitting.png
[settings_files_transfers]:_screenshots_/settings_files_and_transfers.png
[settings_database]:_screenshots_/settings_database.png
[system_notification]:_screenshots_/system_notification.png
[tray_icon]:_screenshots_/tray_icon.png
[database_output]:_screenshots_/database_output.png

## Build Information
* Python 3.7 64-bit
    * PyQt5
    * pyzbar
    * opencv
    * numpy
    * qdarkstyle
    * qimage2ndarray
* Executable built with pyinstaller.
* Installer built with NSIS.
