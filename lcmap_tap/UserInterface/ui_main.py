# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MAIN.UI'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# Edited 7/25/2018 by Dan Zelenak
# - Add Icon to Main Window

from PyQt5 import QtCore, QtGui, QtWidgets
import pkg_resources

class Ui_TAPTool(object):
    def setupUi(self, TAPTool):
        TAPTool.setObjectName("TAPTool")
        TAPTool.resize(957, 609)

        icon = QtGui.QIcon(QtGui.QPixmap(pkg_resources.resource_filename("lcmap_tap",
                                                                         "/".join(("Auxiliary", "icon.PNG")))))
        TAPTool.setWindowIcon(icon)

        TAPTool.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(TAPTool)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.y1line = QtWidgets.QLineEdit(self.centralwidget)
        self.y1line.setMinimumSize(QtCore.QSize(85, 0))
        self.y1line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.y1line.setMaxLength(16)
        self.y1line.setObjectName("y1line")
        self.gridLayout.addWidget(self.y1line, 1, 1, 1, 1)
        self.label_x1 = QtWidgets.QLabel(self.centralwidget)
        self.label_x1.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label_x1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_x1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x1.setObjectName("label_x1")
        self.gridLayout.addWidget(self.label_x1, 0, 0, 1, 1)
        self.comboBoxUnits = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUnits.sizePolicy().hasHeightForWidth())
        self.comboBoxUnits.setSizePolicy(sizePolicy)
        self.comboBoxUnits.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBoxUnits.setObjectName("comboBoxUnits")
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.addItem("")
        self.gridLayout.addWidget(self.comboBoxUnits, 1, 2, 1, 1)
        self.x2line = QtWidgets.QLineEdit(self.centralwidget)
        self.x2line.setEnabled(True)
        self.x2line.setMinimumSize(QtCore.QSize(85, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.x2line.setPalette(palette)
        self.x2line.setAutoFillBackground(False)
        self.x2line.setDragEnabled(False)
        self.x2line.setReadOnly(True)
        self.x2line.setObjectName("x2line")
        self.gridLayout.addWidget(self.x2line, 3, 0, 1, 1)
        self.label_y2 = QtWidgets.QLabel(self.centralwidget)
        self.label_y2.setObjectName("label_y2")
        self.gridLayout.addWidget(self.label_y2, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.x1line = QtWidgets.QLineEdit(self.centralwidget)
        self.x1line.setMinimumSize(QtCore.QSize(85, 0))
        self.x1line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.x1line.setMaxLength(16)
        self.x1line.setObjectName("x1line")
        self.gridLayout.addWidget(self.x1line, 1, 0, 1, 1)
        self.label_units2 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.label_units2.setPalette(palette)
        self.label_units2.setObjectName("label_units2")
        self.gridLayout.addWidget(self.label_units2, 3, 2, 1, 1)
        self.label_x2 = QtWidgets.QLabel(self.centralwidget)
        self.label_x2.setObjectName("label_x2")
        self.gridLayout.addWidget(self.label_x2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_units = QtWidgets.QLabel(self.centralwidget)
        self.label_units.setObjectName("label_units")
        self.gridLayout.addWidget(self.label_units, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_y1 = QtWidgets.QLabel(self.centralwidget)
        self.label_y1.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label_y1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y1.setObjectName("label_y1")
        self.gridLayout.addWidget(self.label_y1, 0, 1, 1, 1)
        self.y2line = QtWidgets.QLineEdit(self.centralwidget)
        self.y2line.setEnabled(True)
        self.y2line.setMinimumSize(QtCore.QSize(85, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.y2line.setPalette(palette)
        self.y2line.setReadOnly(True)
        self.y2line.setObjectName("y2line")
        self.gridLayout.addWidget(self.y2line, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.outputverticalLayout = QtWidgets.QVBoxLayout()
        self.outputverticalLayout.setObjectName("outputverticalLayout")
        self.modelresultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.modelresultsLabel.setObjectName("modelresultsLabel")
        self.outputverticalLayout.addWidget(self.modelresultsLabel)
        self.plainTextEdit_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_results.setReadOnly(True)
        self.plainTextEdit_results.setObjectName("plainTextEdit_results")
        self.outputverticalLayout.addWidget(self.plainTextEdit_results)
        self.clickresultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.clickresultsLabel.setObjectName("clickresultsLabel")
        self.outputverticalLayout.addWidget(self.clickresultsLabel)
        self.clicked_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.clicked_listWidget.setAlternatingRowColors(True)
        self.clicked_listWidget.setObjectName("clicked_listWidget")
        self.outputverticalLayout.addWidget(self.clicked_listWidget)
        self.gridLayout_3.addLayout(self.outputverticalLayout, 0, 2, 13, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.driveLetter_label = QtWidgets.QLabel(self.centralwidget)
        self.driveLetter_label.setObjectName("driveLetter_label")
        self.gridLayout_2.addWidget(self.driveLetter_label, 0, 0, 1, 1)
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setObjectName("version_label")
        self.gridLayout_2.addWidget(self.version_label, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.driveLetter_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.driveLetter_comboBox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.driveLetter_comboBox.setObjectName("driveLetter_comboBox")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.driveLetter_comboBox.addItem("")
        self.gridLayout_2.addWidget(self.driveLetter_comboBox, 1, 0, 1, 1)
        self.version_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.version_comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.version_comboBox.setObjectName("version_comboBox")
        self.gridLayout_2.addWidget(self.version_comboBox, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.json_label = QtWidgets.QLabel(self.centralwidget)
        self.json_label.setObjectName("json_label")
        self.gridLayout_3.addWidget(self.json_label, 2, 0, 1, 1)
        self.horizontalLayout_json = QtWidgets.QHBoxLayout()
        self.horizontalLayout_json.setObjectName("horizontalLayout_json")
        self.browsejsonline = QtWidgets.QLineEdit(self.centralwidget)
        self.browsejsonline.setObjectName("browsejsonline")
        self.horizontalLayout_json.addWidget(self.browsejsonline)
        self.browsejsonbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsejsonbutton.setMinimumSize(QtCore.QSize(25, 0))
        self.browsejsonbutton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.browsejsonbutton.setObjectName("browsejsonbutton")
        self.horizontalLayout_json.addWidget(self.browsejsonbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout_json, 3, 0, 1, 1)
        self.class_label = QtWidgets.QLabel(self.centralwidget)
        self.class_label.setObjectName("class_label")
        self.gridLayout_3.addWidget(self.class_label, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.browseclassline = QtWidgets.QLineEdit(self.centralwidget)
        self.browseclassline.setObjectName("browseclassline")
        self.horizontalLayout_3.addWidget(self.browseclassline)
        self.browseclassbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browseclassbutton.setMinimumSize(QtCore.QSize(25, 0))
        self.browseclassbutton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.browseclassbutton.setObjectName("browseclassbutton")
        self.horizontalLayout_3.addWidget(self.browseclassbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 6, 0, 1, 1)
        self.horizontalLayout_ARD_dir = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ARD_dir.setObjectName("horizontalLayout_ARD_dir")
        self.browseARDline = QtWidgets.QLineEdit(self.centralwidget)
        self.browseARDline.setObjectName("browseARDline")
        self.horizontalLayout_ARD_dir.addWidget(self.browseARDline)
        self.browseardbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browseardbutton.setMinimumSize(QtCore.QSize(25, 0))
        self.browseardbutton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.browseardbutton.setObjectName("browseardbutton")
        self.horizontalLayout_ARD_dir.addWidget(self.browseardbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout_ARD_dir, 7, 0, 1, 1)
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setObjectName("output_label")
        self.gridLayout_3.addWidget(self.output_label, 8, 0, 1, 1)
        self.horizontalLayout_plotsave = QtWidgets.QHBoxLayout()
        self.horizontalLayout_plotsave.setObjectName("horizontalLayout_plotsave")
        self.browseoutputline = QtWidgets.QLineEdit(self.centralwidget)
        self.browseoutputline.setObjectName("browseoutputline")
        self.horizontalLayout_plotsave.addWidget(self.browseoutputline)
        self.browseoutputbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browseoutputbutton.setMinimumSize(QtCore.QSize(25, 0))
        self.browseoutputbutton.setMaximumSize(QtCore.QSize(25, 16777215))
        self.browseoutputbutton.setObjectName("browseoutputbutton")
        self.horizontalLayout_plotsave.addWidget(self.browseoutputbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout_plotsave, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 9, 1, 1, 1)
        self.radioshp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioshp.setChecked(True)
        self.radioshp.setAutoExclusive(False)
        self.radioshp.setObjectName("radioshp")
        self.gridLayout_3.addWidget(self.radioshp, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 11, 1, 1, 1)
        self.listitems = QtWidgets.QListWidget(self.centralwidget)
        self.listitems.setAlternatingRowColors(False)
        self.listitems.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listitems.setObjectName("listitems")
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        self.gridLayout_3.addWidget(self.listitems, 12, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 13, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushLocator = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushLocator.sizePolicy().hasHeightForWidth())
        self.pushLocator.setSizePolicy(sizePolicy)
        self.pushLocator.setMinimumSize(QtCore.QSize(75, 0))
        self.pushLocator.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushLocator.setObjectName("pushLocator")
        self.horizontalLayout_2.addWidget(self.pushLocator)
        self.plotbutton = QtWidgets.QPushButton(self.centralwidget)
        self.plotbutton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotbutton.sizePolicy().hasHeightForWidth())
        self.plotbutton.setSizePolicy(sizePolicy)
        self.plotbutton.setMinimumSize(QtCore.QSize(75, 0))
        self.plotbutton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.plotbutton.setObjectName("plotbutton")
        self.horizontalLayout_2.addWidget(self.plotbutton)
        self.savefigpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savefigpushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savefigpushButton.sizePolicy().hasHeightForWidth())
        self.savefigpushButton.setSizePolicy(sizePolicy)
        self.savefigpushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.savefigpushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.savefigpushButton.setObjectName("savefigpushButton")
        self.horizontalLayout_2.addWidget(self.savefigpushButton)
        self.mapButton = QtWidgets.QPushButton(self.centralwidget)
        self.mapButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapButton.sizePolicy().hasHeightForWidth())
        self.mapButton.setSizePolicy(sizePolicy)
        self.mapButton.setMinimumSize(QtCore.QSize(75, 0))
        self.mapButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.mapButton.setObjectName("mapButton")
        self.horizontalLayout_2.addWidget(self.mapButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 14, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearpushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearpushButton.sizePolicy().hasHeightForWidth())
        self.clearpushButton.setSizePolicy(sizePolicy)
        self.clearpushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.clearpushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.clearpushButton.setObjectName("clearpushButton")
        self.horizontalLayout.addWidget(self.clearpushButton)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton.sizePolicy().hasHeightForWidth())
        self.exitbutton.setSizePolicy(sizePolicy)
        self.exitbutton.setMinimumSize(QtCore.QSize(75, 0))
        self.exitbutton.setMaximumSize(QtCore.QSize(75, 16777215))
        self.exitbutton.setObjectName("exitbutton")
        self.horizontalLayout.addWidget(self.exitbutton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 14, 2, 1, 1)
        TAPTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TAPTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 21))
        self.menubar.setObjectName("menubar")
        TAPTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TAPTool)
        self.statusbar.setObjectName("statusbar")
        TAPTool.setStatusBar(self.statusbar)

        self.retranslateUi(TAPTool)
        self.comboBoxUnits.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TAPTool)
        TAPTool.setTabOrder(self.x1line, self.y1line)
        TAPTool.setTabOrder(self.y1line, self.comboBoxUnits)
        TAPTool.setTabOrder(self.comboBoxUnits, self.browsejsonline)
        TAPTool.setTabOrder(self.browsejsonline, self.browsejsonbutton)
        TAPTool.setTabOrder(self.browsejsonbutton, self.browseARDline)
        TAPTool.setTabOrder(self.browseARDline, self.browseardbutton)
        TAPTool.setTabOrder(self.browseardbutton, self.browseoutputline)
        TAPTool.setTabOrder(self.browseoutputline, self.browseoutputbutton)
        TAPTool.setTabOrder(self.browseoutputbutton, self.radioshp)
        TAPTool.setTabOrder(self.radioshp, self.listitems)
        TAPTool.setTabOrder(self.listitems, self.plotbutton)
        TAPTool.setTabOrder(self.plotbutton, self.savefigpushButton)
        TAPTool.setTabOrder(self.savefigpushButton, self.mapButton)
        TAPTool.setTabOrder(self.mapButton, self.clearpushButton)
        TAPTool.setTabOrder(self.clearpushButton, self.exitbutton)
        TAPTool.setTabOrder(self.exitbutton, self.clicked_listWidget)
        TAPTool.setTabOrder(self.clicked_listWidget, self.plainTextEdit_results)
        TAPTool.setTabOrder(self.plainTextEdit_results, self.y2line)
        TAPTool.setTabOrder(self.y2line, self.x2line)

    def retranslateUi(self, TAPTool):
        _translate = QtCore.QCoreApplication.translate
        TAPTool.setWindowTitle(_translate("TAPTool", "Time Series Analysis and Plotting (TAP) Tool"))
        self.label_x1.setText(_translate("TAPTool", "X (meters)"))
        self.comboBoxUnits.setCurrentText(_translate("TAPTool", "Projected - Meters - Albers CONUS WGS 84"))
        self.comboBoxUnits.setItemText(0, _translate("TAPTool", "Projected - Meters - Albers CONUS WGS 84"))
        self.comboBoxUnits.setItemText(1, _translate("TAPTool", "Geographic - Lat/Long - Decimal Degrees - WGS 84"))
        self.label_y2.setText(_translate("TAPTool", "Lat (dec. deg.)"))
        self.label_units2.setText(_translate("TAPTool", "Geographic - Lat/Long - Decimal Degrees - WGS 84"))
        self.label_x2.setText(_translate("TAPTool", "Long (dec. deg.)"))
        self.label_units.setText(_translate("TAPTool", "Units"))
        self.label_y1.setText(_translate("TAPTool", "Y (meters)"))
        self.modelresultsLabel.setText(_translate("TAPTool", "Model Results:"))
        self.clickresultsLabel.setText(_translate("TAPTool", "Selected Observations:"))
        self.driveLetter_label.setText(_translate("TAPTool", "Eval Server Drive Letter:"))
        self.version_label.setText(_translate("TAPTool", "PyCCD Version"))
        self.driveLetter_comboBox.setItemText(0, _translate("TAPTool", "A:"))
        self.driveLetter_comboBox.setItemText(1, _translate("TAPTool", "B:"))
        self.driveLetter_comboBox.setItemText(2, _translate("TAPTool", "C:"))
        self.driveLetter_comboBox.setItemText(3, _translate("TAPTool", "D:"))
        self.driveLetter_comboBox.setItemText(4, _translate("TAPTool", "E:"))
        self.driveLetter_comboBox.setItemText(5, _translate("TAPTool", "F:"))
        self.driveLetter_comboBox.setItemText(6, _translate("TAPTool", "G:"))
        self.driveLetter_comboBox.setItemText(7, _translate("TAPTool", "H:"))
        self.driveLetter_comboBox.setItemText(8, _translate("TAPTool", "I:"))
        self.driveLetter_comboBox.setItemText(9, _translate("TAPTool", "J:"))
        self.driveLetter_comboBox.setItemText(10, _translate("TAPTool", "K:"))
        self.driveLetter_comboBox.setItemText(11, _translate("TAPTool", "L:"))
        self.driveLetter_comboBox.setItemText(12, _translate("TAPTool", "M:"))
        self.driveLetter_comboBox.setItemText(13, _translate("TAPTool", "N:"))
        self.driveLetter_comboBox.setItemText(14, _translate("TAPTool", "O:"))
        self.driveLetter_comboBox.setItemText(15, _translate("TAPTool", "P:"))
        self.driveLetter_comboBox.setItemText(16, _translate("TAPTool", "Q:"))
        self.driveLetter_comboBox.setItemText(17, _translate("TAPTool", "R:"))
        self.driveLetter_comboBox.setItemText(18, _translate("TAPTool", "S:"))
        self.driveLetter_comboBox.setItemText(19, _translate("TAPTool", "T:"))
        self.driveLetter_comboBox.setItemText(20, _translate("TAPTool", "U:"))
        self.driveLetter_comboBox.setItemText(21, _translate("TAPTool", "V:"))
        self.driveLetter_comboBox.setItemText(22, _translate("TAPTool", "W:"))
        self.driveLetter_comboBox.setItemText(23, _translate("TAPTool", "X:"))
        self.driveLetter_comboBox.setItemText(24, _translate("TAPTool", "Y:"))
        self.driveLetter_comboBox.setItemText(25, _translate("TAPTool", "Z:"))
        self.driveLetter_comboBox.setItemText(26, _translate("TAPTool", "/lcmap_data"))
        self.driveLetter_comboBox.setCurrentText(_translate("TAPTool", "Z:"))
        self.json_label.setText(_translate("TAPTool", "Full path to PyCCD results:"))
        self.browsejsonbutton.setText(_translate("TAPTool", "..."))
        self.class_label.setText(_translate("TAPTool", "Full path to classification results:"))
        self.browseclassbutton.setText(_translate("TAPTool", "..."))
        self.label.setText(_translate("TAPTool", "Full path to ARD .tar files"))
        self.browseardbutton.setText(_translate("TAPTool", "..."))
        self.output_label.setText(_translate("TAPTool", "Output directory to save plots:"))
        self.browseoutputbutton.setText(_translate("TAPTool", "..."))
        self.radioshp.setText(_translate("TAPTool", "Create Point Shapefile on Plot"))
        __sortingEnabled = self.listitems.isSortingEnabled()
        self.listitems.setSortingEnabled(False)
        item = self.listitems.item(0)
        item.setText(_translate("TAPTool", "All Spectral Bands and Indices"))
        item = self.listitems.item(1)
        item.setText(_translate("TAPTool", "All Spectral Bands"))
        item = self.listitems.item(2)
        item.setText(_translate("TAPTool", "All Indices"))
        item = self.listitems.item(3)
        item.setText(_translate("TAPTool", "Blue"))
        item = self.listitems.item(4)
        item.setText(_translate("TAPTool", "Green"))
        item = self.listitems.item(5)
        item.setText(_translate("TAPTool", "Red"))
        item = self.listitems.item(6)
        item.setText(_translate("TAPTool", "NIR"))
        item = self.listitems.item(7)
        item.setText(_translate("TAPTool", "SWIR-1"))
        item = self.listitems.item(8)
        item.setText(_translate("TAPTool", "SWIR-2"))
        item = self.listitems.item(9)
        item.setText(_translate("TAPTool", "Thermal"))
        item = self.listitems.item(10)
        item.setText(_translate("TAPTool", "NDVI"))
        item = self.listitems.item(11)
        item.setText(_translate("TAPTool", "MSAVI"))
        item = self.listitems.item(12)
        item.setText(_translate("TAPTool", "EVI"))
        item = self.listitems.item(13)
        item.setText(_translate("TAPTool", "SAVI"))
        item = self.listitems.item(14)
        item.setText(_translate("TAPTool", "NDMI"))
        item = self.listitems.item(15)
        item.setText(_translate("TAPTool", "NBR"))
        item = self.listitems.item(16)
        item.setText(_translate("TAPTool", "NBR-2"))
        self.listitems.setSortingEnabled(__sortingEnabled)
        self.pushLocator.setText(_translate("TAPTool", "Locator Map"))
        self.plotbutton.setText(_translate("TAPTool", "Plot"))
        self.savefigpushButton.setText(_translate("TAPTool", "Save Figure"))
        self.mapButton.setText(_translate("TAPTool", "Maps"))
        self.clearpushButton.setText(_translate("TAPTool", "Clear"))
        self.exitbutton.setText(_translate("TAPTool", "Close"))

