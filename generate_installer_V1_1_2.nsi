; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "Zebrafish Scan Processor"
!define PRODUCT_VERSION "1.1.2"
!define PRODUCT_PUBLISHER "Sinnhuber Aquatic Research Laboratory"
!define PRODUCT_WEB_SITE "http://www.tanguaylab.com/SARL"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\Zebrafish Scan Processor.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

; MUI 1.67 compatible ------
!include "MUI.nsh"
!include x64.nsh

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!insertmacro MUI_PAGE_LICENSE "license.txt"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\Zebrafish Scan Processor.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "ZScanProcessorSetup_v1_1_2.exe"
InstallDir "$PROGRAMFILES64\Zebrafish Scan Processor"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Function BitTypeTest
  ${IfNot} ${RunningX64}
    MessageBox MB_OK "This software can only be installed on 64-bit systems. Exiting installer."
    abort
  ${EndIf}
FunctionEnd

Function .onInit
  call BitTypeTest
FunctionEnd

Section "Main Application" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite try
  File "Zebrafish Scan Processor\base_library.zip"
  SetOutPath "$INSTDIR\cryptography\hazmat\bindings"
  File "Zebrafish Scan Processor\cryptography\hazmat\bindings\_constant_time.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\cryptography\hazmat\bindings\_openssl.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\cryptography-2.3.1-py3.7.egg-info"
  File "Zebrafish Scan Processor\cryptography-2.3.1-py3.7.egg-info\INSTALLER"
  File "Zebrafish Scan Processor\cryptography-2.3.1-py3.7.egg-info\METADATA"
  File "Zebrafish Scan Processor\cryptography-2.3.1-py3.7.egg-info\RECORD"
  File "Zebrafish Scan Processor\cryptography-2.3.1-py3.7.egg-info\top_level.txt"
  File "Zebrafish Scan Processor\cryptography-2.3.1-py3.7.egg-info\WHEEL"
  SetOutPath "$INSTDIR\cv2"
  File "Zebrafish Scan Processor\cv2\cv2.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\Include"
  File "Zebrafish Scan Processor\Include\pyconfig.h"
  SetOutPath "$INSTDIR\lib2to3"
  File "Zebrafish Scan Processor\lib2to3\Grammar.txt"
  File "Zebrafish Scan Processor\lib2to3\Grammar3.7.0.final.0.pickle"
  File "Zebrafish Scan Processor\lib2to3\PatternGrammar.txt"
  File "Zebrafish Scan Processor\lib2to3\PatternGrammar3.7.0.final.0.pickle"
  SetOutPath "$INSTDIR\lib2to3\tests\data"
  File "Zebrafish Scan Processor\lib2to3\tests\data\README"
  SetOutPath "$INSTDIR"
  File "Zebrafish Scan Processor\libcrypto-1_1-x64.dll"
  File "Zebrafish Scan Processor\libGLESv2.dll"
  File "Zebrafish Scan Processor\libiconv.dll"
  File "Zebrafish Scan Processor\libopenblas.CSRRD7HKRKC3T3YXA7VY7TAZGLSWDKW6.gfortran-win_amd64.dll"
  File "Zebrafish Scan Processor\libssl-1_1-x64.dll"
  File "Zebrafish Scan Processor\libzbar-64.dll"
  File "Zebrafish Scan Processor\logo_small.jpg"
  File "Zebrafish Scan Processor\mfc140u.dll"
  File "Zebrafish Scan Processor\MSVCP140.dll"
  SetOutPath "$INSTDIR\numpy\core"
  File "Zebrafish Scan Processor\numpy\core\multiarray.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\numpy\core\umath.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\numpy\core\_multiarray_tests.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\numpy\fft"
  File "Zebrafish Scan Processor\numpy\fft\fftpack_lite.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\numpy\linalg"
  File "Zebrafish Scan Processor\numpy\linalg\lapack_lite.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\numpy\linalg\_umath_linalg.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\numpy\random"
  File "Zebrafish Scan Processor\numpy\random\mtrand.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\PIL"
  File "Zebrafish Scan Processor\PIL\_imaging.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\PIL\_imagingft.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\PIL\_imagingtk.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\PIL\_webp.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR"
  File "Zebrafish Scan Processor\pyexpat.pyd"
  SetOutPath "$INSTDIR\PyQt5\Qt\bin"
  File "Zebrafish Scan Processor\PyQt5\Qt\bin\d3dcompiler_47.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\bin\libEGL.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\bin\libGLESv2.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\bin\opengl32sw.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\bin\qt.conf"
  SetOutPath "$INSTDIR\PyQt5\Qt\plugins\iconengines"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\iconengines\qsvgicon.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt\plugins\imageformats"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qgif.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qicns.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qico.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qjpeg.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qsvg.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qtga.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qtiff.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qwbmp.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\imageformats\qwebp.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt\plugins\platforms"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\platforms\qminimal.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\platforms\qoffscreen.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\platforms\qwebgl.dll"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\platforms\qwindows.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt\plugins\platformthemes"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\platformthemes\qflatpak.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt\plugins\styles"
  File "Zebrafish Scan Processor\PyQt5\Qt\plugins\styles\qwindowsvistastyle.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt\translations"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_ar.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_bg.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_ca.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_cs.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_da.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_de.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_en.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_es.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_fi.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_fr.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_gd.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_he.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_hu.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_it.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_ja.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_ko.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_lv.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_pl.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_ru.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_sk.qm"
  File "Zebrafish Scan Processor\PyQt5\Qt\translations\qtbase_uk.qm"
  SetOutPath "$INSTDIR\PyQt5"
  File "Zebrafish Scan Processor\PyQt5\QtCore.pyd"
  File "Zebrafish Scan Processor\PyQt5\QtGui.pyd"
  File "Zebrafish Scan Processor\PyQt5\QtWidgets.pyd"
  File "Zebrafish Scan Processor\PyQt5\sip.pyd"
  SetOutPath "$INSTDIR"
  File "Zebrafish Scan Processor\python3.dll"
  File "Zebrafish Scan Processor\python37.dll"
  File "Zebrafish Scan Processor\pythoncom37.dll"
  File "Zebrafish Scan Processor\pywintypes37.dll"
  File "Zebrafish Scan Processor\Qt5Core.dll"
  File "Zebrafish Scan Processor\Qt5DBus.dll"
  File "Zebrafish Scan Processor\Qt5Gui.dll"
  File "Zebrafish Scan Processor\Qt5Network.dll"
  File "Zebrafish Scan Processor\Qt5Qml.dll"
  File "Zebrafish Scan Processor\Qt5Quick.dll"
  File "Zebrafish Scan Processor\Qt5Svg.dll"
  File "Zebrafish Scan Processor\Qt5WebSockets.dll"
  File "Zebrafish Scan Processor\Qt5Widgets.dll"
  File "Zebrafish Scan Processor\Roboto-Regular.ttf"
  File "Zebrafish Scan Processor\select.pyd"
  File "Zebrafish Scan Processor\unicodedata.pyd"
  File "Zebrafish Scan Processor\VCRUNTIME140.dll"
  File "Zebrafish Scan Processor\win32api.pyd"
  SetOutPath "$INSTDIR\win32com\shell"
  File "Zebrafish Scan Processor\win32com\shell\shell.pyd"
  SetOutPath "$INSTDIR"
  File "Zebrafish Scan Processor\win32pdh.pyd"
  File "Zebrafish Scan Processor\win32trace.pyd"
  File "Zebrafish Scan Processor\win32ui.pyd"
  File "Zebrafish Scan Processor\win32wnet.pyd"
  File "Zebrafish Scan Processor\Zebrafish Scan Processor.exe"
  CreateDirectory "$SMPROGRAMS\Zebrafish Scan Processor"
  CreateShortCut "$SMPROGRAMS\Zebrafish Scan Processor\Zebrafish Scan Processor.lnk" "$INSTDIR\Zebrafish Scan Processor.exe"
  CreateShortCut "$DESKTOP\Zebrafish Scan Processor.lnk" "$INSTDIR\Zebrafish Scan Processor.exe"
  File "Zebrafish Scan Processor\Zebrafish Scan Processor.exe.manifest"
  File "Zebrafish Scan Processor\_bz2.pyd"
  File "Zebrafish Scan Processor\_cffi_backend.cp37-win_amd64.pyd"
  File "Zebrafish Scan Processor\_contextvars.pyd"
  File "Zebrafish Scan Processor\_ctypes.pyd"
  File "Zebrafish Scan Processor\_decimal.pyd"
  File "Zebrafish Scan Processor\_distutils_findvs.pyd"
  File "Zebrafish Scan Processor\_hashlib.pyd"
  File "Zebrafish Scan Processor\_lzma.pyd"
  File "Zebrafish Scan Processor\_multiprocessing.pyd"
  File "Zebrafish Scan Processor\_queue.pyd"
  File "Zebrafish Scan Processor\_socket.pyd"
  File "Zebrafish Scan Processor\_ssl.pyd"
  File "Zebrafish Scan Processor\_win32sysloader.pyd"
SectionEnd

Section "Microsoft Visual C++ Redistributable" SEC02
  SetOverwrite ifnewer
  SetOutPath "$INSTDIR"
  File "vcredist_x64.exe"

  ;not installed, so run the installer
  ExecWait '"$INSTDIR\vcredist_x64.exe" /install /passive /norestart'

SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\Zebrafish Scan Processor\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\Zebrafish Scan Processor\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\Zebrafish Scan Processor.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\Zebrafish Scan Processor.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\_win32sysloader.pyd"
  Delete "$INSTDIR\_ssl.pyd"
  Delete "$INSTDIR\_socket.pyd"
  Delete "$INSTDIR\_queue.pyd"
  Delete "$INSTDIR\_multiprocessing.pyd"
  Delete "$INSTDIR\_lzma.pyd"
  Delete "$INSTDIR\_hashlib.pyd"
  Delete "$INSTDIR\_distutils_findvs.pyd"
  Delete "$INSTDIR\_decimal.pyd"
  Delete "$INSTDIR\_ctypes.pyd"
  Delete "$INSTDIR\_contextvars.pyd"
  Delete "$INSTDIR\_cffi_backend.cp37-win_amd64.pyd"
  Delete "$INSTDIR\_bz2.pyd"
  Delete "$INSTDIR\Zebrafish Scan Processor.exe.manifest"
  Delete "$INSTDIR\Zebrafish Scan Processor.exe"
  Delete "$INSTDIR\win32wnet.pyd"
  Delete "$INSTDIR\win32ui.pyd"
  Delete "$INSTDIR\win32trace.pyd"
  Delete "$INSTDIR\win32pdh.pyd"
  Delete "$INSTDIR\win32com\shell\shell.pyd"
  Delete "$INSTDIR\win32api.pyd"
  Delete "$INSTDIR\VCRUNTIME140.dll"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\Roboto-Regular.ttf"
  Delete "$INSTDIR\Qt5Widgets.dll"
  Delete "$INSTDIR\Qt5WebSockets.dll"
  Delete "$INSTDIR\Qt5Svg.dll"
  Delete "$INSTDIR\Qt5Quick.dll"
  Delete "$INSTDIR\Qt5Qml.dll"
  Delete "$INSTDIR\Qt5Network.dll"
  Delete "$INSTDIR\Qt5Gui.dll"
  Delete "$INSTDIR\Qt5DBus.dll"
  Delete "$INSTDIR\Qt5Core.dll"
  Delete "$INSTDIR\pywintypes37.dll"
  Delete "$INSTDIR\pythoncom37.dll"
  Delete "$INSTDIR\python37.dll"
  Delete "$INSTDIR\python3.dll"
  Delete "$INSTDIR\PyQt5\sip.pyd"
  Delete "$INSTDIR\PyQt5\QtWidgets.pyd"
  Delete "$INSTDIR\PyQt5\QtGui.pyd"
  Delete "$INSTDIR\PyQt5\QtCore.pyd"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_uk.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_sk.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_ru.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_pl.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_lv.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_ko.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_ja.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_it.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_hu.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_he.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_gd.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_fr.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_fi.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_es.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_en.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_de.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_da.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_cs.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_ca.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_bg.qm"
  Delete "$INSTDIR\PyQt5\Qt\translations\qtbase_ar.qm"
  Delete "$INSTDIR\PyQt5\Qt\plugins\styles\qwindowsvistastyle.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\platformthemes\qflatpak.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\platforms\qwindows.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\platforms\qwebgl.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\platforms\qoffscreen.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\platforms\qminimal.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qwebp.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qwbmp.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qtiff.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qtga.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qsvg.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qjpeg.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qico.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qicns.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\imageformats\qgif.dll"
  Delete "$INSTDIR\PyQt5\Qt\plugins\iconengines\qsvgicon.dll"
  Delete "$INSTDIR\PyQt5\Qt\bin\qt.conf"
  Delete "$INSTDIR\PyQt5\Qt\bin\opengl32sw.dll"
  Delete "$INSTDIR\PyQt5\Qt\bin\libGLESv2.dll"
  Delete "$INSTDIR\PyQt5\Qt\bin\libEGL.dll"
  Delete "$INSTDIR\PyQt5\Qt\bin\d3dcompiler_47.dll"
  Delete "$INSTDIR\pyexpat.pyd"
  Delete "$INSTDIR\PIL\_webp.cp37-win_amd64.pyd"
  Delete "$INSTDIR\PIL\_imagingtk.cp37-win_amd64.pyd"
  Delete "$INSTDIR\PIL\_imagingft.cp37-win_amd64.pyd"
  Delete "$INSTDIR\PIL\_imaging.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\mtrand.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\linalg\_umath_linalg.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\linalg\lapack_lite.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\fft\fftpack_lite.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\core\_multiarray_tests.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\core\umath.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\core\multiarray.cp37-win_amd64.pyd"
  Delete "$INSTDIR\MSVCP140.dll"
  Delete "$INSTDIR\mfc140u.dll"
  Delete "$INSTDIR\logo_small.jpg"
  Delete "$INSTDIR\libzbar-64.dll"
  Delete "$INSTDIR\libssl-1_1-x64.dll"
  Delete "$INSTDIR\libopenblas.CSRRD7HKRKC3T3YXA7VY7TAZGLSWDKW6.gfortran-win_amd64.dll"
  Delete "$INSTDIR\libiconv.dll"
  Delete "$INSTDIR\libGLESv2.dll"
  Delete "$INSTDIR\libcrypto-1_1-x64.dll"
  Delete "$INSTDIR\lib2to3\tests\data\README"
  Delete "$INSTDIR\lib2to3\PatternGrammar3.7.0.final.0.pickle"
  Delete "$INSTDIR\lib2to3\PatternGrammar.txt"
  Delete "$INSTDIR\lib2to3\Grammar3.7.0.final.0.pickle"
  Delete "$INSTDIR\lib2to3\Grammar.txt"
  Delete "$INSTDIR\Include\pyconfig.h"
  Delete "$INSTDIR\cv2\cv2.cp37-win_amd64.pyd"
  Delete "$INSTDIR\cryptography-2.3.1-py3.7.egg-info\WHEEL"
  Delete "$INSTDIR\cryptography-2.3.1-py3.7.egg-info\top_level.txt"
  Delete "$INSTDIR\cryptography-2.3.1-py3.7.egg-info\RECORD"
  Delete "$INSTDIR\cryptography-2.3.1-py3.7.egg-info\METADATA"
  Delete "$INSTDIR\cryptography-2.3.1-py3.7.egg-info\INSTALLER"
  Delete "$INSTDIR\cryptography\hazmat\bindings\_openssl.cp37-win_amd64.pyd"
  Delete "$INSTDIR\cryptography\hazmat\bindings\_constant_time.cp37-win_amd64.pyd"
  Delete "$INSTDIR\base_library.zip"
  Delete "$INSTDIR\vcredist_x64.exe"

  Delete "$SMPROGRAMS\Zebrafish Scan Processor\Uninstall.lnk"
  Delete "$SMPROGRAMS\Zebrafish Scan Processor\Website.lnk"
  Delete "$DESKTOP\Zebrafish Scan Processor.lnk"
  Delete "$SMPROGRAMS\Zebrafish Scan Processor\Zebrafish Scan Processor.lnk"

  RMDir "$SMPROGRAMS\Zebrafish Scan Processor"
  RMDir "$INSTDIR\win32com\shell"
  RMDir "$INSTDIR\win32com"
  RMDir "$INSTDIR\PyQt5\Qt\translations"
  RMDir "$INSTDIR\PyQt5\Qt\plugins\styles"
  RMDir "$INSTDIR\PyQt5\Qt\plugins\platformthemes"
  RMDir "$INSTDIR\PyQt5\Qt\plugins\platforms"
  RMDir "$INSTDIR\PyQt5\Qt\plugins\imageformats"
  RMDir "$INSTDIR\PyQt5\Qt\plugins\iconengines"
  RMDir "$INSTDIR\PyQt5\Qt\plugins"
  RMDir "$INSTDIR\PyQt5\Qt\bin"
  RMDir "$INSTDIR\PyQt5\Qt"
  RMDir "$INSTDIR\PyQt5"
  RMDir "$INSTDIR\PIL"
  RMDir "$INSTDIR\numpy\random"
  RMDir "$INSTDIR\numpy\linalg"
  RMDir "$INSTDIR\numpy\fft"
  RMDir "$INSTDIR\numpy\core"
  RMDir "$INSTDIR\numpy"
  RMDir "$INSTDIR\lib2to3\tests\data"
  RMDir "$INSTDIR\lib2to3\tests"
  RMDir "$INSTDIR\lib2to3"
  RMDir "$INSTDIR\Include"
  RMDir "$INSTDIR\cv2"
  RMDir "$INSTDIR\cryptography-2.3.1-py3.7.egg-info"
  RMDir "$INSTDIR\cryptography\hazmat\bindings"
  RMDir "$INSTDIR\cryptography\hazmat"
  RMDir "$INSTDIR\cryptography"
  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd