# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZScanUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1536, 1024)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1536, 1024))
        MainWindow.setMaximumSize(QtCore.QSize(1536, 1024))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLine{\n"
"    background-color:rgb(202, 202, 202);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_39 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_11.addWidget(self.label_39)
        self.live_log_info_checkbox = QtWidgets.QCheckBox(self.tab_6)
        self.live_log_info_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.live_log_info_checkbox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 1px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color:green;\n"
"}\n"
"\n"
"QCheckBox::indicator:!checked{\n"
"    background-color:rgb(55,55,55);\n"
"}")
        self.live_log_info_checkbox.setChecked(True)
        self.live_log_info_checkbox.setObjectName("live_log_info_checkbox")
        self.horizontalLayout_11.addWidget(self.live_log_info_checkbox)
        self.line_7 = QtWidgets.QFrame(self.tab_6)
        self.line_7.setStyleSheet("Line{\n"
"\n"
"background-color:rgb(202, 202, 202);\n"
"}")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_11.addWidget(self.line_7)
        self.live_log_warning_checkbox = QtWidgets.QCheckBox(self.tab_6)
        self.live_log_warning_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.live_log_warning_checkbox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 1px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color:green;\n"
"}\n"
"\n"
"QCheckBox::indicator:!checked{\n"
"    background-color:rgb(55,55,55);\n"
"}")
        self.live_log_warning_checkbox.setChecked(True)
        self.live_log_warning_checkbox.setObjectName("live_log_warning_checkbox")
        self.horizontalLayout_11.addWidget(self.live_log_warning_checkbox)
        self.line_8 = QtWidgets.QFrame(self.tab_6)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_11.addWidget(self.line_8)
        self.live_log_error_checkbox = QtWidgets.QCheckBox(self.tab_6)
        self.live_log_error_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.live_log_error_checkbox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 1px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color:green;\n"
"}\n"
"\n"
"QCheckBox::indicator:!checked{\n"
"    background-color:rgb(55,55,55);\n"
"}")
        self.live_log_error_checkbox.setChecked(True)
        self.live_log_error_checkbox.setObjectName("live_log_error_checkbox")
        self.horizontalLayout_11.addWidget(self.live_log_error_checkbox)
        self.line_9 = QtWidgets.QFrame(self.tab_6)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_11.addWidget(self.line_9)
        self.live_log_debug_checkbox = QtWidgets.QCheckBox(self.tab_6)
        self.live_log_debug_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.live_log_debug_checkbox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 1px solid rgb(55,55,55);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-color:green;\n"
"}\n"
"\n"
"QCheckBox::indicator:!checked{\n"
"    background-color:rgb(55,55,55);\n"
"}")
        self.live_log_debug_checkbox.setChecked(False)
        self.live_log_debug_checkbox.setObjectName("live_log_debug_checkbox")
        self.horizontalLayout_11.addWidget(self.live_log_debug_checkbox)
        self.line_10 = QtWidgets.QFrame(self.tab_6)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_11.addWidget(self.line_10)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.live_log_text_browser = QtWidgets.QTextBrowser(self.tab_6)
        self.live_log_text_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.live_log_text_browser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.live_log_text_browser.setObjectName("live_log_text_browser")
        self.gridLayout_5.addWidget(self.live_log_text_browser, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(1470, 498))
        self.label_11.setMaximumSize(QtCore.QSize(1470, 498))
        self.label_11.setStyleSheet("background-color:black;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.horizontalLayout_4.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_6.addWidget(self.label_25)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setObjectName("label_27")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setObjectName("label_28")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setObjectName("label_29")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setObjectName("label_30")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setObjectName("label_31")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_4.setObjectName("spinBox_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_4)
        self.spinBox_5 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_5.setObjectName("spinBox_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_5)
        self.spinBox_6 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_6.setObjectName("spinBox_6")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_6)
        self.spinBox_7 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_7.setObjectName("spinBox_7")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_7)
        self.spinBox_8 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_8.setObjectName("spinBox_8")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_8)
        self.verticalLayout_6.addLayout(self.formLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.line_6 = QtWidgets.QFrame(self.tab_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_7.addWidget(self.line_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setObjectName("label_32")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setObjectName("label_33")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        self.label_34.setObjectName("label_34")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.label_35 = QtWidgets.QLabel(self.tab_3)
        self.label_35.setObjectName("label_35")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.label_36 = QtWidgets.QLabel(self.tab_3)
        self.label_36.setObjectName("label_36")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setObjectName("label_37")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.label_38 = QtWidgets.QLabel(self.tab_3)
        self.label_38.setObjectName("label_38")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.spinBox_9 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_9.setObjectName("spinBox_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_9)
        self.spinBox_10 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_10.setObjectName("spinBox_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_10)
        self.spinBox_11 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_11.setObjectName("spinBox_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_11)
        self.spinBox_12 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_12.setObjectName("spinBox_12")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinBox_12)
        self.spinBox_13 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_13.setObjectName("spinBox_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBox_13)
        self.spinBox_14 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_14.setObjectName("spinBox_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_14)
        self.spinBox_15 = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox_15.setObjectName("spinBox_15")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_15)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 4, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(736, 498))
        self.label_14.setMaximumSize(QtCore.QSize(736, 498))
        self.label_14.setStyleSheet("background-color:black;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(self.tab_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_10.addWidget(self.line_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)
        self.barcode_preview_top_raw_label = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_preview_top_raw_label.sizePolicy().hasHeightForWidth())
        self.barcode_preview_top_raw_label.setSizePolicy(sizePolicy)
        self.barcode_preview_top_raw_label.setMinimumSize(QtCore.QSize(450, 45))
        self.barcode_preview_top_raw_label.setStyleSheet("background-color:black;")
        self.barcode_preview_top_raw_label.setText("")
        self.barcode_preview_top_raw_label.setScaledContents(False)
        self.barcode_preview_top_raw_label.setObjectName("barcode_preview_top_raw_label")
        self.gridLayout_4.addWidget(self.barcode_preview_top_raw_label, 0, 1, 1, 1)
        self.barcode_preview_top_raw_label_2 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_preview_top_raw_label_2.sizePolicy().hasHeightForWidth())
        self.barcode_preview_top_raw_label_2.setSizePolicy(sizePolicy)
        self.barcode_preview_top_raw_label_2.setMinimumSize(QtCore.QSize(450, 45))
        self.barcode_preview_top_raw_label_2.setStyleSheet("background-color:black;")
        self.barcode_preview_top_raw_label_2.setText("")
        self.barcode_preview_top_raw_label_2.setScaledContents(False)
        self.barcode_preview_top_raw_label_2.setObjectName("barcode_preview_top_raw_label_2")
        self.gridLayout_4.addWidget(self.barcode_preview_top_raw_label_2, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 0, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.tab_3)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_3.addWidget(self.line_16, 5, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_57 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_15.addWidget(self.label_57)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.label_58 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        self.label_58.setMinimumSize(QtCore.QSize(736, 498))
        self.label_58.setMaximumSize(QtCore.QSize(736, 498))
        self.label_58.setStyleSheet("background-color:black;")
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.verticalLayout_9.addWidget(self.label_58)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        self.line_12 = QtWidgets.QFrame(self.tab_4)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_14.addWidget(self.line_12)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_59 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_16.addWidget(self.label_59)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem16)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_60 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.gridLayout_7.addWidget(self.label_60, 2, 0, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.tab_4)
        self.label_61.setObjectName("label_61")
        self.gridLayout_7.addWidget(self.label_61, 2, 1, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.gridLayout_7.addWidget(self.label_62, 1, 0, 1, 1)
        self.barcode_preview_top_raw_label_3 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_preview_top_raw_label_3.sizePolicy().hasHeightForWidth())
        self.barcode_preview_top_raw_label_3.setSizePolicy(sizePolicy)
        self.barcode_preview_top_raw_label_3.setMinimumSize(QtCore.QSize(450, 45))
        self.barcode_preview_top_raw_label_3.setStyleSheet("background-color:black;")
        self.barcode_preview_top_raw_label_3.setText("")
        self.barcode_preview_top_raw_label_3.setScaledContents(False)
        self.barcode_preview_top_raw_label_3.setObjectName("barcode_preview_top_raw_label_3")
        self.gridLayout_7.addWidget(self.barcode_preview_top_raw_label_3, 0, 1, 1, 1)
        self.barcode_preview_top_raw_label_4 = QtWidgets.QLabel(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcode_preview_top_raw_label_4.sizePolicy().hasHeightForWidth())
        self.barcode_preview_top_raw_label_4.setSizePolicy(sizePolicy)
        self.barcode_preview_top_raw_label_4.setMinimumSize(QtCore.QSize(450, 45))
        self.barcode_preview_top_raw_label_4.setStyleSheet("background-color:black;")
        self.barcode_preview_top_raw_label_4.setText("")
        self.barcode_preview_top_raw_label_4.setScaledContents(False)
        self.barcode_preview_top_raw_label_4.setObjectName("barcode_preview_top_raw_label_4")
        self.gridLayout_7.addWidget(self.barcode_preview_top_raw_label_4, 1, 1, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.gridLayout_7.addWidget(self.label_63, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem17, 0, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem18, 1, 2, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_7)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem19)
        self.horizontalLayout_14.addLayout(self.verticalLayout_10)
        self.gridLayout_8.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_56 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_13.addWidget(self.label_56)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem20)
        self.gridLayout_8.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.tab_4)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_8.addWidget(self.line_13, 1, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_40 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_7.addWidget(self.label_40)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_41 = QtWidgets.QLabel(self.tab_4)
        self.label_41.setObjectName("label_41")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.spinBox_16 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_16.setObjectName("spinBox_16")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_16)
        self.label_42 = QtWidgets.QLabel(self.tab_4)
        self.label_42.setObjectName("label_42")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.label_43 = QtWidgets.QLabel(self.tab_4)
        self.label_43.setObjectName("label_43")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.label_44 = QtWidgets.QLabel(self.tab_4)
        self.label_44.setObjectName("label_44")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.label_45 = QtWidgets.QLabel(self.tab_4)
        self.label_45.setObjectName("label_45")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.label_46 = QtWidgets.QLabel(self.tab_4)
        self.label_46.setObjectName("label_46")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.spinBox_17 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_17.setObjectName("spinBox_17")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_17)
        self.spinBox_18 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_18.setObjectName("spinBox_18")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_18)
        self.spinBox_19 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_19.setObjectName("spinBox_19")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_19)
        self.spinBox_20 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_20.setObjectName("spinBox_20")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_20)
        self.spinBox_21 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_21.setObjectName("spinBox_21")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_21)
        self.verticalLayout_7.addLayout(self.formLayout_4)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem21)
        self.horizontalLayout_12.addLayout(self.verticalLayout_7)
        self.line_11 = QtWidgets.QFrame(self.tab_4)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_12.addWidget(self.line_11)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_47 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_8.addWidget(self.label_47)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_48 = QtWidgets.QLabel(self.tab_4)
        self.label_48.setObjectName("label_48")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_48)
        self.spinBox_22 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_22.setObjectName("spinBox_22")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_22)
        self.label_49 = QtWidgets.QLabel(self.tab_4)
        self.label_49.setObjectName("label_49")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.label_50 = QtWidgets.QLabel(self.tab_4)
        self.label_50.setObjectName("label_50")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.label_51 = QtWidgets.QLabel(self.tab_4)
        self.label_51.setObjectName("label_51")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_51)
        self.label_52 = QtWidgets.QLabel(self.tab_4)
        self.label_52.setObjectName("label_52")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_52)
        self.label_53 = QtWidgets.QLabel(self.tab_4)
        self.label_53.setObjectName("label_53")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.label_54 = QtWidgets.QLabel(self.tab_4)
        self.label_54.setObjectName("label_54")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.label_55 = QtWidgets.QLabel(self.tab_4)
        self.label_55.setObjectName("label_55")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_55)
        self.spinBox_23 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_23.setObjectName("spinBox_23")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_23)
        self.spinBox_24 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_24.setObjectName("spinBox_24")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_24)
        self.spinBox_25 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_25.setObjectName("spinBox_25")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_25)
        self.spinBox_26 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_26.setObjectName("spinBox_26")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinBox_26)
        self.spinBox_27 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_27.setObjectName("spinBox_27")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinBox_27)
        self.spinBox_28 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_28.setObjectName("spinBox_28")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_28)
        self.spinBox_29 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_29.setObjectName("spinBox_29")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_29)
        self.verticalLayout_8.addLayout(self.formLayout_5)
        self.horizontalLayout_12.addLayout(self.verticalLayout_8)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem22)
        self.gridLayout_8.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem23, 4, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_64 = QtWidgets.QLabel(self.tab_4)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_17.addWidget(self.label_64)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_17.addWidget(self.progressBar_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_17, 6, 0, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.tab_4)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_8.addWidget(self.line_15, 5, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_72 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_18.addWidget(self.label_72)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem24)
        self.gridLayout_9.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.file_transfer_failed_rename_images_browse_button = QtWidgets.QPushButton(self.tab_5)
        self.file_transfer_failed_rename_images_browse_button.setObjectName("file_transfer_failed_rename_images_browse_button")
        self.gridLayout_15.addWidget(self.file_transfer_failed_rename_images_browse_button, 1, 2, 1, 1)
        self.file_transfer_failed_rename_images_line_edit = QtWidgets.QLineEdit(self.tab_5)
        self.file_transfer_failed_rename_images_line_edit.setObjectName("file_transfer_failed_rename_images_line_edit")
        self.gridLayout_15.addWidget(self.file_transfer_failed_rename_images_line_edit, 1, 1, 1, 1)
        self.file_transfer_input_images_line_edit = QtWidgets.QLineEdit(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_transfer_input_images_line_edit.sizePolicy().hasHeightForWidth())
        self.file_transfer_input_images_line_edit.setSizePolicy(sizePolicy)
        self.file_transfer_input_images_line_edit.setMinimumSize(QtCore.QSize(750, 0))
        self.file_transfer_input_images_line_edit.setObjectName("file_transfer_input_images_line_edit")
        self.gridLayout_15.addWidget(self.file_transfer_input_images_line_edit, 0, 1, 1, 1)
        self.file_transfer_local_output_line_edit = QtWidgets.QLineEdit(self.tab_5)
        self.file_transfer_local_output_line_edit.setObjectName("file_transfer_local_output_line_edit")
        self.gridLayout_15.addWidget(self.file_transfer_local_output_line_edit, 2, 1, 1, 1)
        self.file_transfer_local_output_browse_button = QtWidgets.QPushButton(self.tab_5)
        self.file_transfer_local_output_browse_button.setObjectName("file_transfer_local_output_browse_button")
        self.gridLayout_15.addWidget(self.file_transfer_local_output_browse_button, 2, 2, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.gridLayout_15.addWidget(self.label_67, 2, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.gridLayout_15.addWidget(self.label_68, 1, 0, 1, 1)
        self.file_transfer_input_images_browse_button = QtWidgets.QPushButton(self.tab_5)
        self.file_transfer_input_images_browse_button.setObjectName("file_transfer_input_images_browse_button")
        self.gridLayout_15.addWidget(self.file_transfer_input_images_browse_button, 0, 2, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setToolTip("")
        self.label_66.setToolTipDuration(-1)
        self.label_66.setObjectName("label_66")
        self.gridLayout_15.addWidget(self.label_66, 3, 0, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.gridLayout_15.addWidget(self.label_65, 0, 0, 1, 1)
        self.file_transfer_network_transfer_browse_button = QtWidgets.QPushButton(self.tab_5)
        self.file_transfer_network_transfer_browse_button.setObjectName("file_transfer_network_transfer_browse_button")
        self.gridLayout_15.addWidget(self.file_transfer_network_transfer_browse_button, 3, 2, 1, 1)
        self.file_transfer_network_transfer_line_edit = QtWidgets.QLineEdit(self.tab_5)
        self.file_transfer_network_transfer_line_edit.setObjectName("file_transfer_network_transfer_line_edit")
        self.gridLayout_15.addWidget(self.file_transfer_network_transfer_line_edit, 3, 1, 1, 1)
        self.horizontalLayout_20.addLayout(self.gridLayout_15)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem25)
        self.gridLayout_9.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.tab_5)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_9.addWidget(self.line_14, 2, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_73 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_19.addWidget(self.label_73)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem26)
        self.gridLayout_9.addLayout(self.horizontalLayout_19, 3, 0, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_71 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout_18.addWidget(self.label_71, 0, 0, 1, 1)
        self.file_transfer_transfer_time_edit = QtWidgets.QTimeEdit(self.tab_5)
        self.file_transfer_transfer_time_edit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.file_transfer_transfer_time_edit.setObjectName("file_transfer_transfer_time_edit")
        self.gridLayout_18.addWidget(self.file_transfer_transfer_time_edit, 0, 1, 1, 1)
        self.horizontalLayout_21.addLayout(self.gridLayout_18)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem27)
        self.gridLayout_9.addLayout(self.horizontalLayout_21, 4, 0, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 671, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem28, 5, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.label_81 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.gridLayout_43.addWidget(self.label_81, 0, 1, 1, 1)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.tab_7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setStyleSheet("")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.gridLayout_43.addWidget(self.textBrowser_9, 1, 1, 1, 1)
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.about_revision_label = QtWidgets.QLabel(self.tab_7)
        self.about_revision_label.setObjectName("about_revision_label")
        self.gridLayout_44.addWidget(self.about_revision_label, 1, 1, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.tab_7)
        self.label_82.setObjectName("label_82")
        self.gridLayout_44.addWidget(self.label_82, 0, 0, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.tab_7)
        self.label_84.setObjectName("label_84")
        self.gridLayout_44.addWidget(self.label_84, 1, 0, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.tab_7)
        self.label_83.setObjectName("label_83")
        self.gridLayout_44.addWidget(self.label_83, 0, 1, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.tab_7)
        self.label_88.setObjectName("label_88")
        self.gridLayout_44.addWidget(self.label_88, 3, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_44.addItem(spacerItem29, 5, 0, 1, 1)
        self.about_author_label = QtWidgets.QLabel(self.tab_7)
        self.about_author_label.setOpenExternalLinks(True)
        self.about_author_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.about_author_label.setObjectName("about_author_label")
        self.gridLayout_44.addWidget(self.about_author_label, 2, 1, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.tab_7)
        self.label_85.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_85.setObjectName("label_85")
        self.gridLayout_44.addWidget(self.label_85, 2, 0, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.tab_7)
        self.label_91.setText("")
        self.label_91.setObjectName("label_91")
        self.gridLayout_44.addWidget(self.label_91, 3, 1, 1, 1)
        self.gridLayout_43.addLayout(self.gridLayout_44, 1, 0, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.gridLayout_43.addWidget(self.label_80, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_43, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_39.setText(_translate("MainWindow", "Displayed:"))
        self.live_log_info_checkbox.setText(_translate("MainWindow", "Info"))
        self.live_log_warning_checkbox.setText(_translate("MainWindow", "Warning"))
        self.live_log_error_checkbox.setText(_translate("MainWindow", "Error"))
        self.live_log_debug_checkbox.setText(_translate("MainWindow", "Debug"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Logs"))
        self.label.setText(_translate("MainWindow", "Preview Image Path:"))
        self.label_2.setText(_translate("MainWindow", "C:\\Users\\temp\\Pictures\\23423423.tif"))
        self.label_3.setText(_translate("MainWindow", "Preview Image Info:"))
        self.label_4.setText(_translate("MainWindow", "X Size:"))
        self.label_6.setText(_translate("MainWindow", "2544 px"))
        self.label_5.setText(_translate("MainWindow", "Y Size:"))
        self.label_7.setText(_translate("MainWindow", "3556 px"))
        self.label_8.setText(_translate("MainWindow", "File Size:"))
        self.label_9.setText(_translate("MainWindow", "450 MB"))
        self.pushButton.setText(_translate("MainWindow", "Set Preview Image"))
        self.label_10.setText(_translate("MainWindow", "Preview Image"))
        self.label_12.setText(_translate("MainWindow", "Settings"))
        self.label_13.setText(_translate("MainWindow", "Plate Split Line Location"))
        self.spinBox.setSuffix(_translate("MainWindow", " px"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Plate Splitting"))
        self.label_16.setText(_translate("MainWindow", "Settings"))
        self.label_25.setText(_translate("MainWindow", "Alignment and Limits"))
        self.label_26.setText(_translate("MainWindow", "TextLabel"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "TextLabel"))
        self.label_29.setText(_translate("MainWindow", "TextLabel"))
        self.label_30.setText(_translate("MainWindow", "TextLabel"))
        self.label_31.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "Barcode Detection"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.label_32.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "TextLabel"))
        self.label_34.setText(_translate("MainWindow", "TextLabel"))
        self.label_35.setText(_translate("MainWindow", "TextLabel"))
        self.label_36.setText(_translate("MainWindow", "TextLabel"))
        self.label_37.setText(_translate("MainWindow", "TextLabel"))
        self.label_38.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "Detection Processing Status"))
        self.label_15.setText(_translate("MainWindow", "Top Plate Preview Image"))
        self.label_18.setText(_translate("MainWindow", "Barcode Detection"))
        self.label_21.setText(_translate("MainWindow", "Barcode Value"))
        self.label_22.setText(_translate("MainWindow", "N/A"))
        self.label_19.setText(_translate("MainWindow", "Threshold Image"))
        self.label_17.setText(_translate("MainWindow", "Original Image"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Top Plate"))
        self.label_57.setText(_translate("MainWindow", "Bottom Plate Preview Image"))
        self.label_59.setText(_translate("MainWindow", "Barcode Detection"))
        self.label_60.setText(_translate("MainWindow", "Barcode Value"))
        self.label_61.setText(_translate("MainWindow", "N/A"))
        self.label_62.setText(_translate("MainWindow", "Threshold Image"))
        self.label_63.setText(_translate("MainWindow", "Original Image"))
        self.label_56.setText(_translate("MainWindow", "Settings"))
        self.label_40.setText(_translate("MainWindow", "Alignment and Limits"))
        self.label_41.setText(_translate("MainWindow", "TextLabel"))
        self.label_42.setText(_translate("MainWindow", "TextLabel"))
        self.label_43.setText(_translate("MainWindow", "TextLabel"))
        self.label_44.setText(_translate("MainWindow", "TextLabel"))
        self.label_45.setText(_translate("MainWindow", "TextLabel"))
        self.label_46.setText(_translate("MainWindow", "TextLabel"))
        self.label_47.setText(_translate("MainWindow", "Barcode Detection"))
        self.label_48.setText(_translate("MainWindow", "TextLabel"))
        self.label_49.setText(_translate("MainWindow", "TextLabel"))
        self.label_50.setText(_translate("MainWindow", "TextLabel"))
        self.label_51.setText(_translate("MainWindow", "TextLabel"))
        self.label_52.setText(_translate("MainWindow", "TextLabel"))
        self.label_53.setText(_translate("MainWindow", "TextLabel"))
        self.label_54.setText(_translate("MainWindow", "TextLabel"))
        self.label_55.setText(_translate("MainWindow", "TextLabel"))
        self.label_64.setText(_translate("MainWindow", "Detection Processing Status"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Bottom Plate"))
        self.label_72.setText(_translate("MainWindow", "File Storage"))
        self.file_transfer_failed_rename_images_browse_button.setText(_translate("MainWindow", "Browse"))
        self.file_transfer_failed_rename_images_line_edit.setText(_translate("MainWindow", "*** No Path Set ***"))
        self.file_transfer_input_images_line_edit.setText(_translate("MainWindow", "*** No Path Set ***"))
        self.file_transfer_local_output_line_edit.setText(_translate("MainWindow", "*** No Path Set ***"))
        self.file_transfer_local_output_browse_button.setText(_translate("MainWindow", "Browse"))
        self.label_67.setText(_translate("MainWindow", "Local Output Images Directory"))
        self.label_68.setText(_translate("MainWindow", "Failed Renamed Images Directory"))
        self.file_transfer_input_images_browse_button.setText(_translate("MainWindow", "Browse"))
        self.label_66.setText(_translate("MainWindow", "Network Transfer Directory"))
        self.label_65.setText(_translate("MainWindow", "Input Images Directory"))
        self.file_transfer_network_transfer_browse_button.setText(_translate("MainWindow", "Browse"))
        self.file_transfer_network_transfer_line_edit.setText(_translate("MainWindow", "*** No Path Set ***"))
        self.label_73.setText(_translate("MainWindow", "Network Transfers"))
        self.label_71.setText(_translate("MainWindow", "Transfer Time"))
        self.file_transfer_transfer_time_edit.setDisplayFormat(_translate("MainWindow", "hh:mm AP"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Files and Transfers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Settings"))
        self.label_81.setText(_translate("MainWindow", "Licenses"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">                    GNU GENERAL PUBLIC LICENSE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">                       Version 3, 29 June 2007</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"> Copyright (C) 2007 Free Software Foundation, Inc. &lt;http://fsf.org/&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"> Everyone is permitted to copy and distribute verbatim copies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"> of this license document, but changing it is not allowed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">                            Preamble</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The GNU General Public License is a free, copyleft license for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">software and other kinds of works.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The licenses for most software and other practical works are designed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to take away your freedom to share and change the works.  By contrast,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the GNU General Public License is intended to guarantee your freedom to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">share and change all versions of a program--to make sure it remains free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">software for all its users.  We, the Free Software Foundation, use the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">GNU General Public License for most of our software; it applies also to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">any other work released this way by its authors.  You can apply it to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">your programs, too.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  When we speak of free software, we are referring to freedom, not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">price.  Our General Public Licenses are designed to make sure that you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">have the freedom to distribute copies of free software (and charge for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">them if you wish), that you receive source code or can get it if you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">want it, that you can change the software or use pieces of it in new</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">free programs, and that you know you can do these things.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  To protect your rights, we need to prevent others from denying you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">these rights or asking you to surrender the rights.  Therefore, you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">certain responsibilities if you distribute copies of the software, or if</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">you modify it: responsibilities to respect the freedom of others.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  For example, if you distribute copies of such a program, whether</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">gratis or for a fee, you must pass on to the recipients the same</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">freedoms that you received.  You must make sure that they, too, receive</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">or can get the source code.  And you must show them these terms so they</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">know their rights.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Developers that use the GNU GPL protect your rights with two steps:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">(1) assert copyright on the software, and (2) offer you this License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">giving you legal permission to copy, distribute and/or modify it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  For the developers\' and authors\' protection, the GPL clearly explains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">that there is no warranty for this free software.  For both users\' and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">authors\' sake, the GPL requires that modified versions be marked as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">changed, so that their problems will not be attributed erroneously to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">authors of previous versions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Some devices are designed to deny users access to install or run</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modified versions of the software inside them, although the manufacturer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">can do so.  This is fundamentally incompatible with the aim of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">protecting users\' freedom to change the software.  The systematic</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">pattern of such abuse occurs in the area of products for individuals to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">use, which is precisely where it is most unacceptable.  Therefore, we</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">have designed this version of the GPL to prohibit the practice for those</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">products.  If such problems arise substantially in other domains, we</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">stand ready to extend this provision to those domains in future versions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">of the GPL, as needed to protect the freedom of users.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Finally, every program is threatened constantly by software patents.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">States should not allow patents to restrict development and use of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">software on general-purpose computers, but in those that do, we wish to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">avoid the special danger that patents applied to a free program could</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">make it effectively proprietary.  To prevent this, the GPL assures that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">patents cannot be used to render the program non-free.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The precise terms and conditions for copying, distribution and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modification follow.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">                       TERMS AND CONDITIONS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  0. Definitions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  &quot;This License&quot; refers to version 3 of the GNU General Public License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  &quot;Copyright&quot; also means copyright-like laws that apply to other kinds of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">works, such as semiconductor masks.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  &quot;The Program&quot; refers to any copyrightable work licensed under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License.  Each licensee is addressed as &quot;you&quot;.  &quot;Licensees&quot; and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">&quot;recipients&quot; may be individuals or organizations.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  To &quot;modify&quot; a work means to copy from or adapt all or part of the work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in a fashion requiring copyright permission, other than the making of an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">exact copy.  The resulting work is called a &quot;modified version&quot; of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">earlier work or a work &quot;based on&quot; the earlier work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A &quot;covered work&quot; means either the unmodified Program or a work based</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">on the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  To &quot;propagate&quot; a work means to do anything with it that, without</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">permission, would make you directly or secondarily liable for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">infringement under applicable copyright law, except executing it on a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">computer or modifying a private copy.  Propagation includes copying,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">distribution (with or without modification), making available to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">public, and in some countries other activities as well.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  To &quot;convey&quot; a work means any kind of propagation that enables other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">parties to make or receive copies.  Mere interaction with a user through</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">a computer network, with no transfer of a copy, is not conveying.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  An interactive user interface displays &quot;Appropriate Legal Notices&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to the extent that it includes a convenient and prominently visible</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">feature that (1) displays an appropriate copyright notice, and (2)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">tells the user that there is no warranty for the work (except to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">extent that warranties are provided), that licensees may convey the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">work under this License, and how to view a copy of this License.  If</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the interface presents a list of user commands or options, such as a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">menu, a prominent item in the list meets this criterion.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  1. Source Code.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The &quot;source code&quot; for a work means the preferred form of the work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">for making modifications to it.  &quot;Object code&quot; means any non-source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">form of a work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A &quot;Standard Interface&quot; means an interface that either is an official</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">standard defined by a recognized standards body, or, in the case of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">interfaces specified for a particular programming language, one that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">is widely used among developers working in that language.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The &quot;System Libraries&quot; of an executable work include anything, other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">than the work as a whole, that (a) is included in the normal form of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">packaging a Major Component, but which is not part of that Major</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Component, and (b) serves only to enable use of the work with that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Major Component, or to implement a Standard Interface for which an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">implementation is available to the public in source code form.  A</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">&quot;Major Component&quot;, in this context, means a major essential component</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">(kernel, window system, and so on) of the specific operating system</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">(if any) on which the executable work runs, or a compiler used to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">produce the work, or an object code interpreter used to run it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The &quot;Corresponding Source&quot; for a work in object code form means all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the source code needed to generate, install, and (for an executable</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">work) run the object code and to modify the work, including scripts to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">control those activities.  However, it does not include the work\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">System Libraries, or general-purpose tools or generally available free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">programs which are used unmodified in performing those activities but</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">which are not part of the work.  For example, Corresponding Source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">includes interface definition files associated with source files for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the work, and the source code for shared libraries and dynamically</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">linked subprograms that the work is specifically designed to require,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">such as by intimate data communication or control flow between those</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">subprograms and other parts of the work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The Corresponding Source need not include anything that users</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">can regenerate automatically from other parts of the Corresponding</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Source.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The Corresponding Source for a work in source code form is that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">same work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  2. Basic Permissions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  All rights granted under this License are granted for the term of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">copyright on the Program, and are irrevocable provided the stated</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">conditions are met.  This License explicitly affirms your unlimited</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">permission to run the unmodified Program.  The output from running a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">covered work is covered by this License only if the output, given its</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">content, constitutes a covered work.  This License acknowledges your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">rights of fair use or other equivalent, as provided by copyright law.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may make, run and propagate covered works that you do not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">convey, without conditions so long as your license otherwise remains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in force.  You may convey covered works to others for the sole purpose</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">of having them make modifications exclusively for you, or provide you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">with facilities for running those works, provided that you comply with</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the terms of this License in conveying all material for which you do</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">not control copyright.  Those thus making or running the covered works</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">for you must do so exclusively on your behalf, under your direction</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">and control, on terms that prohibit them from making any copies of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">your copyrighted material outside their relationship with you.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Conveying under any other circumstances is permitted solely under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the conditions stated below.  Sublicensing is not allowed; section 10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">makes it unnecessary.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  3. Protecting Users\' Legal Rights From Anti-Circumvention Law.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  No covered work shall be deemed part of an effective technological</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">measure under any applicable law fulfilling obligations under article</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">11 of the WIPO copyright treaty adopted on 20 December 1996, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">similar laws prohibiting or restricting circumvention of such</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">measures.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  When you convey a covered work, you waive any legal power to forbid</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">circumvention of technological measures to the extent such circumvention</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">is effected by exercising rights under this License with respect to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the covered work, and you disclaim any intention to limit operation or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modification of the work as a means of enforcing, against the work\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">users, your or third parties\' legal rights to forbid circumvention of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">technological measures.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  4. Conveying Verbatim Copies.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may convey verbatim copies of the Program\'s source code as you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">receive it, in any medium, provided that you conspicuously and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">appropriately publish on each copy an appropriate copyright notice;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">keep intact all notices stating that this License and any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">non-permissive terms added in accord with section 7 apply to the code;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">keep intact all notices of the absence of any warranty; and give all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">recipients a copy of this License along with the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may charge any price or no price for each copy that you convey,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">and you may offer support or warranty protection for a fee.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  5. Conveying Modified Source Versions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may convey a work based on the Program, or the modifications to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">produce it from the Program, in the form of source code under the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">terms of section 4, provided that you also meet all of these conditions:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    a) The work must carry prominent notices stating that you modified</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    it, and giving a relevant date.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    b) The work must carry prominent notices stating that it is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    released under this License and any conditions added under section</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    7.  This requirement modifies the requirement in section 4 to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    &quot;keep intact all notices&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    c) You must license the entire work, as a whole, under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    License to anyone who comes into possession of a copy.  This</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    License will therefore apply, along with any applicable section 7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    additional terms, to the whole of the work, and all its parts,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    regardless of how they are packaged.  This License gives no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    permission to license the work in any other way, but it does not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    invalidate such permission if you have separately received it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    d) If the work has interactive user interfaces, each must display</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Appropriate Legal Notices; however, if the Program has interactive</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    interfaces that do not display Appropriate Legal Notices, your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    work need not make them do so.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A compilation of a covered work with other separate and independent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">works, which are not by their nature extensions of the covered work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">and which are not combined with it such as to form a larger program,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in or on a volume of a storage or distribution medium, is called an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">&quot;aggregate&quot; if the compilation and its resulting copyright are not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">used to limit the access or legal rights of the compilation\'s users</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">beyond what the individual works permit.  Inclusion of a covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in an aggregate does not cause this License to apply to the other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">parts of the aggregate.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  6. Conveying Non-Source Forms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may convey a covered work in object code form under the terms</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">of sections 4 and 5, provided that you also convey the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">machine-readable Corresponding Source under the terms of this License,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in one of these ways:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    a) Convey the object code in, or embodied in, a physical product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    (including a physical distribution medium), accompanied by the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Corresponding Source fixed on a durable physical medium</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    customarily used for software interchange.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    b) Convey the object code in, or embodied in, a physical product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    (including a physical distribution medium), accompanied by a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    written offer, valid for at least three years and valid for as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    long as you offer spare parts or customer support for that product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    model, to give anyone who possesses the object code either (1) a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    copy of the Corresponding Source for all the software in the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    product that is covered by this License, on a durable physical</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    medium customarily used for software interchange, for a price no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    more than your reasonable cost of physically performing this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    conveying of source, or (2) access to copy the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Corresponding Source from a network server at no charge.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    c) Convey individual copies of the object code with a copy of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    written offer to provide the Corresponding Source.  This</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    alternative is allowed only occasionally and noncommercially, and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    only if you received the object code with such an offer, in accord</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    with subsection 6b.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    d) Convey the object code by offering access from a designated</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    place (gratis or for a charge), and offer equivalent access to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Corresponding Source in the same way through the same place at no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    further charge.  You need not require recipients to copy the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Corresponding Source along with the object code.  If the place to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    copy the object code is a network server, the Corresponding Source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    may be on a different server (operated by you or a third party)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    that supports equivalent copying facilities, provided you maintain</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    clear directions next to the object code saying where to find the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Corresponding Source.  Regardless of what server hosts the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Corresponding Source, you remain obligated to ensure that it is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    available for as long as needed to satisfy these requirements.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    e) Convey the object code using peer-to-peer transmission, provided</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    you inform other peers where the object code and Corresponding</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Source of the work are being offered to the general public at no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    charge under subsection 6d.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A separable portion of the object code, whose source code is excluded</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">from the Corresponding Source as a System Library, need not be</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">included in conveying the object code work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A &quot;User Product&quot; is either (1) a &quot;consumer product&quot;, which means any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">tangible personal property which is normally used for personal, family,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">or household purposes, or (2) anything designed or sold for incorporation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">into a dwelling.  In determining whether a product is a consumer product,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">doubtful cases shall be resolved in favor of coverage.  For a particular</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">product received by a particular user, &quot;normally used&quot; refers to a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">typical or common use of that class of product, regardless of the status</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">of the particular user or of the way in which the particular user</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">actually uses, or expects or is expected to use, the product.  A product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">is a consumer product regardless of whether the product has substantial</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">commercial, industrial or non-consumer uses, unless such uses represent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the only significant mode of use of the product.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  &quot;Installation Information&quot; for a User Product means any methods,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">procedures, authorization keys, or other information required to install</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">and execute modified versions of a covered work in that User Product from</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">a modified version of its Corresponding Source.  The information must</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">suffice to ensure that the continued functioning of the modified object</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">code is in no case prevented or interfered with solely because</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modification has been made.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If you convey an object code work under this section in, or with, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">specifically for use in, a User Product, and the conveying occurs as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">part of a transaction in which the right of possession and use of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">User Product is transferred to the recipient in perpetuity or for a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">fixed term (regardless of how the transaction is characterized), the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Corresponding Source conveyed under this section must be accompanied</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">by the Installation Information.  But this requirement does not apply</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">if neither you nor any third party retains the ability to install</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modified object code on the User Product (for example, the work has</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">been installed in ROM).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The requirement to provide Installation Information does not include a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">requirement to continue to provide support service, warranty, or updates</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">for a work that has been modified or installed by the recipient, or for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the User Product in which it has been modified or installed.  Access to a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">network may be denied when the modification itself materially and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">adversely affects the operation of the network or violates the rules and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">protocols for communication across the network.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Corresponding Source conveyed, and Installation Information provided,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in accord with this section must be in a format that is publicly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">documented (and with an implementation available to the public in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">source code form), and must require no special password or key for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">unpacking, reading or copying.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  7. Additional Terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  &quot;Additional permissions&quot; are terms that supplement the terms of this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License by making exceptions from one or more of its conditions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Additional permissions that are applicable to the entire Program shall</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">be treated as though they were included in this License, to the extent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">that they are valid under applicable law.  If additional permissions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">apply only to part of the Program, that part may be used separately</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">under those permissions, but the entire Program remains governed by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">this License without regard to the additional permissions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  When you convey a copy of a covered work, you may at your option</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">remove any additional permissions from that copy, or from any part of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">it.  (Additional permissions may be written to require their own</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">removal in certain cases when you modify the work.)  You may place</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">additional permissions on material, added by you to a covered work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">for which you have or can give appropriate copyright permission.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Notwithstanding any other provision of this License, for material you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">add to a covered work, you may (if authorized by the copyright holders of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">that material) supplement the terms of this License with terms:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    a) Disclaiming warranty or limiting liability differently from the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    terms of sections 15 and 16 of this License; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    b) Requiring preservation of specified reasonable legal notices or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    author attributions in that material or in the Appropriate Legal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Notices displayed by works containing it; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    c) Prohibiting misrepresentation of the origin of that material, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    requiring that modified versions of such material be marked in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    reasonable ways as different from the original version; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    d) Limiting the use for publicity purposes of names of licensors or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    authors of the material; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    e) Declining to grant rights under trademark law for use of some</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    trade names, trademarks, or service marks; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    f) Requiring indemnification of licensors and authors of that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    material by anyone who conveys the material (or modified versions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    it) with contractual assumptions of liability to the recipient, for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    any liability that these contractual assumptions directly impose on</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    those licensors and authors.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  All other non-permissive additional terms are considered &quot;further</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">restrictions&quot; within the meaning of section 10.  If the Program as you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">received it, or any part of it, contains a notice stating that it is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">governed by this License along with a term that is a further</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">restriction, you may remove that term.  If a license document contains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">a further restriction but permits relicensing or conveying under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License, you may add to a covered work material governed by the terms</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">of that license document, provided that the further restriction does</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">not survive such relicensing or conveying.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If you add terms to a covered work in accord with this section, you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">must place, in the relevant source files, a statement of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">additional terms that apply to those files, or a notice indicating</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">where to find the applicable terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Additional terms, permissive or non-permissive, may be stated in the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">form of a separately written license, or stated as exceptions;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the above requirements apply either way.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  8. Termination.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may not propagate or modify a covered work except as expressly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">provided under this License.  Any attempt otherwise to propagate or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modify it is void, and will automatically terminate your rights under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">this License (including any patent licenses granted under the third</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">paragraph of section 11).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  However, if you cease all violation of this License, then your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">license from a particular copyright holder is reinstated (a)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">provisionally, unless and until the copyright holder explicitly and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">finally terminates your license, and (b) permanently, if the copyright</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">holder fails to notify you of the violation by some reasonable means</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">prior to 60 days after the cessation.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Moreover, your license from a particular copyright holder is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">reinstated permanently if the copyright holder notifies you of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">violation by some reasonable means, this is the first time you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">received notice of violation of this License (for any work) from that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">copyright holder, and you cure the violation prior to 30 days after</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">your receipt of the notice.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Termination of your rights under this section does not terminate the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">licenses of parties who have received copies or rights from you under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">this License.  If your rights have been terminated and not permanently</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">reinstated, you do not qualify to receive new licenses for the same</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">material under section 10.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  9. Acceptance Not Required for Having Copies.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You are not required to accept this License in order to receive or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">run a copy of the Program.  Ancillary propagation of a covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">occurring solely as a consequence of using peer-to-peer transmission</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to receive a copy likewise does not require acceptance.  However,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">nothing other than this License grants you permission to propagate or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">modify any covered work.  These actions infringe copyright if you do</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">not accept this License.  Therefore, by modifying or propagating a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">covered work, you indicate your acceptance of this License to do so.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  10. Automatic Licensing of Downstream Recipients.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Each time you convey a covered work, the recipient automatically</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">receives a license from the original licensors, to run, modify and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">propagate that work, subject to this License.  You are not responsible</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">for enforcing compliance by third parties with this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  An &quot;entity transaction&quot; is a transaction transferring control of an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">organization, or substantially all assets of one, or subdividing an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">organization, or merging organizations.  If propagation of a covered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">work results from an entity transaction, each party to that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">transaction who receives a copy of the work also receives whatever</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">licenses to the work the party\'s predecessor in interest had or could</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">give under the previous paragraph, plus a right to possession of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Corresponding Source of the work from the predecessor in interest, if</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the predecessor has it or can get it with reasonable efforts.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You may not impose any further restrictions on the exercise of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">rights granted or affirmed under this License.  For example, you may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">not impose a license fee, royalty, or other charge for exercise of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">rights granted under this License, and you may not initiate litigation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">(including a cross-claim or counterclaim in a lawsuit) alleging that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">any patent claim is infringed by making, using, selling, offering for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">sale, or importing the Program or any portion of it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  11. Patents.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A &quot;contributor&quot; is a copyright holder who authorizes use under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License of the Program or a work on which the Program is based.  The</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">work thus licensed is called the contributor\'s &quot;contributor version&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A contributor\'s &quot;essential patent claims&quot; are all patent claims</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">owned or controlled by the contributor, whether already acquired or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">hereafter acquired, that would be infringed by some manner, permitted</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">by this License, of making, using, or selling its contributor version,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">but do not include claims that would be infringed only as a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">consequence of further modification of the contributor version.  For</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">purposes of this definition, &quot;control&quot; includes the right to grant</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">patent sublicenses in a manner consistent with the requirements of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Each contributor grants you a non-exclusive, worldwide, royalty-free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">patent license under the contributor\'s essential patent claims, to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">make, use, sell, offer for sale, import and otherwise run, modify and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">propagate the contents of its contributor version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  In the following three paragraphs, a &quot;patent license&quot; is any express</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">agreement or commitment, however denominated, not to enforce a patent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">(such as an express permission to practice a patent or covenant not to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">sue for patent infringement).  To &quot;grant&quot; such a patent license to a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">party means to make such an agreement or commitment not to enforce a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">patent against the party.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If you convey a covered work, knowingly relying on a patent license,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">and the Corresponding Source of the work is not available for anyone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to copy, free of charge and under the terms of this License, through a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">publicly available network server or other readily accessible means,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">then you must either (1) cause the Corresponding Source to be so</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">available, or (2) arrange to deprive yourself of the benefit of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">patent license for this particular work, or (3) arrange, in a manner</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">consistent with the requirements of this License, to extend the patent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">license to downstream recipients.  &quot;Knowingly relying&quot; means you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">actual knowledge that, but for the patent license, your conveying the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">covered work in a country, or your recipient\'s use of the covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in a country, would infringe one or more identifiable patents in that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">country that you have reason to believe are valid.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If, pursuant to or in connection with a single transaction or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">arrangement, you convey, or propagate by procuring conveyance of, a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">covered work, and grant a patent license to some of the parties</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">receiving the covered work authorizing them to use, propagate, modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">or convey a specific copy of the covered work, then the patent license</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">you grant is automatically extended to all recipients of the covered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">work and works based on it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  A patent license is &quot;discriminatory&quot; if it does not include within</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the scope of its coverage, prohibits the exercise of, or is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">conditioned on the non-exercise of one or more of the rights that are</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">specifically granted under this License.  You may not convey a covered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">work if you are a party to an arrangement with a third party that is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">in the business of distributing software, under which you make payment</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to the third party based on the extent of your activity of conveying</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the work, and under which the third party grants, to any of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">parties who would receive the covered work from you, a discriminatory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">patent license (a) in connection with copies of the covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">conveyed by you (or copies made from those copies), or (b) primarily</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">for and in connection with specific products or compilations that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">contain the covered work, unless you entered into that arrangement,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">or that patent license was granted, prior to 28 March 2007.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Nothing in this License shall be construed as excluding or limiting</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">any implied license or other defenses to infringement that may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">otherwise be available to you under applicable patent law.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  12. No Surrender of Others\' Freedom.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If conditions are imposed on you (whether by court order, agreement or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">otherwise) that contradict the conditions of this License, they do not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">excuse you from the conditions of this License.  If you cannot convey a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">covered work so as to satisfy simultaneously your obligations under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License and any other pertinent obligations, then as a consequence you may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">not convey it at all.  For example, if you agree to terms that obligate you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to collect a royalty for further conveying from those to whom you convey</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the Program, the only way you could satisfy both those terms and this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License would be to refrain entirely from conveying the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  13. Use with the GNU Affero General Public License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Notwithstanding any other provision of this License, you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">permission to link or combine any covered work with a work licensed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">under version 3 of the GNU Affero General Public License into a single</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">combined work, and to convey the resulting work.  The terms of this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">License will continue to apply to the part which is the covered work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">but the special requirements of the GNU Affero General Public License,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">section 13, concerning interaction through a network will apply to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">combination as such.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  14. Revised Versions of this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The Free Software Foundation may publish revised and/or new versions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the GNU General Public License from time to time.  Such new versions will</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">be similar in spirit to the present version, but may differ in detail to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">address new problems or concerns.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Each version is given a distinguishing version number.  If the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Program specifies that a certain numbered version of the GNU General</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Public License &quot;or any later version&quot; applies to it, you have the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">option of following the terms and conditions either of that numbered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">version or of any later version published by the Free Software</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Foundation.  If the Program does not specify a version number of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">GNU General Public License, you may choose any version ever published</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">by the Free Software Foundation.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If the Program specifies that a proxy can decide which future</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">versions of the GNU General Public License can be used, that proxy\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">public statement of acceptance of a version permanently authorizes you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to choose that version for the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  Later license versions may give you additional or different</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">permissions.  However, no additional obligations are imposed on any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">author or copyright holder as a result of your choosing to follow a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  15. Disclaimer of Warranty.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM &quot;AS IS&quot; WITHOUT WARRANTY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">ALL NECESSARY SERVICING, REPAIR OR CORRECTION.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  16. Limitation of Liability.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">SUCH DAMAGES.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  17. Interpretation of Sections 15 and 16.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If the disclaimer of warranty and limitation of liability provided</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">above cannot be given local legal effect according to their terms,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">reviewing courts shall apply local law that most closely approximates</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">an absolute waiver of all civil liability in connection with the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Program, unless a warranty or assumption of liability accompanies a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">copy of the Program in return for a fee.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">                     END OF TERMS AND CONDITIONS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">            How to Apply These Terms to Your New Programs</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If you develop a new program, and you want it to be of the greatest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">possible use to the public, the best way to achieve this is to make it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">free software which everyone can redistribute and change under these terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  To do so, attach the following notices to the program.  It is safest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">to attach them to the start of each source file to most effectively</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">state the exclusion of warranty; and each file should have at least</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the &quot;copyright&quot; line and a pointer to where the full notice is found.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    &lt;one line to give the program\'s name and a brief idea of what it does.&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    This program is free software: you can redistribute it and/or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    the Free Software Foundation, either version 3 of the License, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    (at your option) any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    You should have received a copy of the GNU General Public License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Also add information on how to contact you by electronic and paper mail.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  If the program does terminal interaction, make it output a short</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">notice like this when it starts in an interactive mode:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    This is free software, and you are welcome to redistribute it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">    under certain conditions; type `show c\' for details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">The hypothetical commands `show w\' and `show c\' should show the appropriate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">parts of the General Public License.  Of course, your program\'s commands</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">might be different; for a GUI interface, you would use an &quot;about box&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  You should also get your employer (if you work as a programmer) or school,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">if any, to sign a &quot;copyright disclaimer&quot; for the program, if necessary.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">For more information on this, and how to apply and follow the GNU GPL, see</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">&lt;http://www.gnu.org/licenses/&gt;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">  The GNU General Public License does not permit incorporating your program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">into proprietary programs.  If your program is a subroutine library, you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">may consider it more useful to permit linking proprietary applications with</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">the library.  If this is what you want to do, use the GNU Lesser General</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">Public License instead of this License.  But first, please read</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:8pt; color:#000000;\">&lt;http://www.gnu.org/philosophy/why-not-lgpl.html&gt;</span></p></body></html>"))
        self.about_revision_label.setText(_translate("MainWindow", "0.1"))
        self.label_82.setText(_translate("MainWindow", "Application Name:"))
        self.label_84.setText(_translate("MainWindow", "Revision #:"))
        self.label_83.setText(_translate("MainWindow", "ZScan Processor"))
        self.label_88.setText(_translate("MainWindow", "Contributor(s):"))
        self.about_author_label.setText(_translate("MainWindow", "<html><head/><body><p>Corwin Perren</p><p>caperren@caperren.com</p><p><a href=\"http:\\\\www.caperren.com\"><span style=\" text-decoration: underline; color:rgb(169, 69, 0);\">http:\\\\www.caperren.com</span></a></p></body></html>"))
        self.label_85.setText(_translate("MainWindow", "Author(s):"))
        self.label_80.setText(_translate("MainWindow", "About"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "About"))
