# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyCCDPlottingTool(object):
    def setupUi(self, PyCCDPlottingTool):
        PyCCDPlottingTool.setObjectName("PyCCDPlottingTool")
        PyCCDPlottingTool.resize(417, 772)
        PyCCDPlottingTool.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(PyCCDPlottingTool)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_main = QtWidgets.QGridLayout()
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.radioshp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioshp.setChecked(True)
        self.radioshp.setObjectName("radioshp")
        self.gridLayout_main.addWidget(self.radioshp, 14, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_main.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_main.addWidget(self.label_6, 9, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_main.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_plotsave = QtWidgets.QHBoxLayout()
        self.horizontalLayout_plotsave.setObjectName("horizontalLayout_plotsave")
        self.browseoutputline = QtWidgets.QLineEdit(self.centralwidget)
        self.browseoutputline.setObjectName("browseoutputline")
        self.horizontalLayout_plotsave.addWidget(self.browseoutputline)
        self.browseoutputbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browseoutputbutton.setObjectName("browseoutputbutton")
        self.horizontalLayout_plotsave.addWidget(self.browseoutputbutton)
        self.gridLayout_main.addLayout(self.horizontalLayout_plotsave, 10, 0, 1, 1)
        self.horizontalLayout_hvLabels = QtWidgets.QHBoxLayout()
        self.horizontalLayout_hvLabels.setObjectName("horizontalLayout_hvLabels")
        self.label_h = QtWidgets.QLabel(self.centralwidget)
        self.label_h.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_h.setAlignment(QtCore.Qt.AlignCenter)
        self.label_h.setObjectName("label_h")
        self.horizontalLayout_hvLabels.addWidget(self.label_h)
        self.label_v = QtWidgets.QLabel(self.centralwidget)
        self.label_v.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_v.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v.setObjectName("label_v")
        self.horizontalLayout_hvLabels.addWidget(self.label_v)
        self.gridLayout_main.addLayout(self.horizontalLayout_hvLabels, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem, 22, 0, 1, 1)
        self.arccoordsline = QtWidgets.QLineEdit(self.centralwidget)
        self.arccoordsline.setObjectName("arccoordsline")
        self.gridLayout_main.addWidget(self.arccoordsline, 1, 0, 1, 1)
        self.horizontalLayout_cache = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cache.setObjectName("horizontalLayout_cache")
        self.browsecacheline = QtWidgets.QLineEdit(self.centralwidget)
        self.browsecacheline.setObjectName("browsecacheline")
        self.horizontalLayout_cache.addWidget(self.browsecacheline)
        self.browsecachebutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsecachebutton.setObjectName("browsecachebutton")
        self.horizontalLayout_cache.addWidget(self.browsecachebutton)
        self.gridLayout_main.addLayout(self.horizontalLayout_cache, 6, 0, 1, 1)
        self.horizontalLayout_json = QtWidgets.QHBoxLayout()
        self.horizontalLayout_json.setObjectName("horizontalLayout_json")
        self.browsejsonline = QtWidgets.QLineEdit(self.centralwidget)
        self.browsejsonline.setObjectName("browsejsonline")
        self.horizontalLayout_json.addWidget(self.browsejsonline)
        self.browsejsonbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsejsonbutton.setObjectName("browsejsonbutton")
        self.horizontalLayout_json.addWidget(self.browsejsonbutton)
        self.gridLayout_main.addLayout(self.horizontalLayout_json, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_main.addWidget(self.label_3, 7, 0, 1, 1)
        self.radiomasked = QtWidgets.QRadioButton(self.centralwidget)
        self.radiomasked.setChecked(True)
        self.radiomasked.setAutoExclusive(False)
        self.radiomasked.setObjectName("radiomasked")
        self.gridLayout_main.addWidget(self.radiomasked, 13, 0, 1, 1)
        self.horizontalLayout_hvinput = QtWidgets.QHBoxLayout()
        self.horizontalLayout_hvinput.setObjectName("horizontalLayout_hvinput")
        self.hline = QtWidgets.QLineEdit(self.centralwidget)
        self.hline.setMaximumSize(QtCore.QSize(50, 16777215))
        self.hline.setMaxLength(2)
        self.hline.setObjectName("hline")
        self.horizontalLayout_hvinput.addWidget(self.hline)
        self.vline = QtWidgets.QLineEdit(self.centralwidget)
        self.vline.setMaximumSize(QtCore.QSize(50, 16777215))
        self.vline.setMaxLength(2)
        self.vline.setObjectName("vline")
        self.horizontalLayout_hvinput.addWidget(self.vline)
        self.gridLayout_main.addLayout(self.horizontalLayout_hvinput, 4, 0, 1, 1)
        self.radiomodelfit = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radiomodelfit.sizePolicy().hasHeightForWidth())
        self.radiomodelfit.setSizePolicy(sizePolicy)
        self.radiomodelfit.setChecked(True)
        self.radiomodelfit.setAutoExclusive(False)
        self.radiomodelfit.setObjectName("radiomodelfit")
        self.gridLayout_main.addWidget(self.radiomodelfit, 12, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_xmin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xmin.setObjectName("lineEdit_xmin")
        self.gridLayout_3.addWidget(self.lineEdit_xmin, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lineEdit_ymax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ymax.setObjectName("lineEdit_ymax")
        self.gridLayout_3.addWidget(self.lineEdit_ymax, 1, 1, 1, 1)
        self.lineEdit_ymin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ymin.setObjectName("lineEdit_ymin")
        self.gridLayout_3.addWidget(self.lineEdit_ymin, 5, 1, 1, 1)
        self.lineEdit_xmax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xmax.setObjectName("lineEdit_xmax")
        self.gridLayout_3.addWidget(self.lineEdit_xmax, 3, 2, 1, 1)
        self.label_ymax = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax.setObjectName("label_ymax")
        self.gridLayout_3.addWidget(self.label_ymax, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_ymin = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin.setObjectName("label_ymin")
        self.gridLayout_3.addWidget(self.label_ymin, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_xmin = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin.setObjectName("label_xmin")
        self.gridLayout_3.addWidget(self.label_xmin, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_xmax = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax.setAlignment(QtCore.Qt.AlignCenter)
        self.label_xmax.setObjectName("label_xmax")
        self.gridLayout_3.addWidget(self.label_xmax, 2, 2, 1, 1)
        self.gridLayout_main.addLayout(self.gridLayout_3, 19, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_main.addItem(spacerItem1, 2, 0, 1, 1)
        self.plainTextEdit_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_results.setReadOnly(True)
        self.plainTextEdit_results.setObjectName("plainTextEdit_results")
        self.gridLayout_main.addWidget(self.plainTextEdit_results, 23, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem2, 15, 0, 1, 1)
        self.comboBox_bands = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_bands.setEditable(False)
        self.comboBox_bands.setObjectName("comboBox_bands")
        self.comboBox_bands.addItem("")
        self.comboBox_bands.addItem("")
        self.comboBox_bands.addItem("")
        self.comboBox_bands.addItem("")
        self.comboBox_bands.addItem("")
        self.comboBox_bands.addItem("")
        self.comboBox_bands.addItem("")
        self.gridLayout_main.addWidget(self.comboBox_bands, 18, 0, 1, 1)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton.sizePolicy().hasHeightForWidth())
        self.exitbutton.setSizePolicy(sizePolicy)
        self.exitbutton.setMinimumSize(QtCore.QSize(100, 0))
        self.exitbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.exitbutton.setObjectName("exitbutton")
        self.gridLayout_main.addWidget(self.exitbutton, 21, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.plotbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotbutton.sizePolicy().hasHeightForWidth())
        self.plotbutton.setSizePolicy(sizePolicy)
        self.plotbutton.setMinimumSize(QtCore.QSize(100, 0))
        self.plotbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.plotbutton.setPalette(palette)
        self.plotbutton.setObjectName("plotbutton")
        self.gridLayout_main.addWidget(self.plotbutton, 16, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem3, 11, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem4, 20, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem5, 17, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_main, 0, 0, 1, 1)
        PyCCDPlottingTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyCCDPlottingTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 21))
        self.menubar.setObjectName("menubar")
        PyCCDPlottingTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyCCDPlottingTool)
        self.statusbar.setObjectName("statusbar")
        PyCCDPlottingTool.setStatusBar(self.statusbar)

        self.retranslateUi(PyCCDPlottingTool)
        QtCore.QMetaObject.connectSlotsByName(PyCCDPlottingTool)

    def retranslateUi(self, PyCCDPlottingTool):
        _translate = QtCore.QCoreApplication.translate
        PyCCDPlottingTool.setWindowTitle(_translate("PyCCDPlottingTool", "PyCCD Plotting Tool"))
        self.radioshp.setText(_translate("PyCCDPlottingTool", "Create Point Shapefile on Plot"))
        self.label_2.setText(_translate("PyCCDPlottingTool", "Full path to cache folder:"))
        self.label_6.setText(_translate("PyCCDPlottingTool", "Output directory to save plots:"))
        self.label.setText(_translate("PyCCDPlottingTool", "Paste coordinates directly from ArcMap:"))
        self.browseoutputbutton.setText(_translate("PyCCDPlottingTool", "..."))
        self.label_h.setText(_translate("PyCCDPlottingTool", "h"))
        self.label_v.setText(_translate("PyCCDPlottingTool", "v"))
        self.browsecachebutton.setText(_translate("PyCCDPlottingTool", "..."))
        self.browsejsonbutton.setText(_translate("PyCCDPlottingTool", "..."))
        self.label_3.setText(_translate("PyCCDPlottingTool", "Full path to JSON folder:"))
        self.radiomasked.setText(_translate("PyCCDPlottingTool", "Draw Masked Observations"))
        self.radiomodelfit.setText(_translate("PyCCDPlottingTool", "Draw Model Fit"))
        self.label_ymax.setText(_translate("PyCCDPlottingTool", "Y Max"))
        self.label_ymin.setText(_translate("PyCCDPlottingTool", "Y Min"))
        self.label_xmin.setText(_translate("PyCCDPlottingTool", "X Min"))
        self.label_xmax.setText(_translate("PyCCDPlottingTool", "X Max"))
        self.comboBox_bands.setItemText(0, _translate("PyCCDPlottingTool", "Band 1"))
        self.comboBox_bands.setItemText(1, _translate("PyCCDPlottingTool", "Band 2"))
        self.comboBox_bands.setItemText(2, _translate("PyCCDPlottingTool", "Band 3"))
        self.comboBox_bands.setItemText(3, _translate("PyCCDPlottingTool", "Band 4"))
        self.comboBox_bands.setItemText(4, _translate("PyCCDPlottingTool", "Band 5"))
        self.comboBox_bands.setItemText(5, _translate("PyCCDPlottingTool", "Band 6"))
        self.comboBox_bands.setItemText(6, _translate("PyCCDPlottingTool", "Band 7"))
        self.exitbutton.setText(_translate("PyCCDPlottingTool", "Close"))
        self.plotbutton.setText(_translate("PyCCDPlottingTool", "Plot"))

