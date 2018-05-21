# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MAPS_VIEWER_dev.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapViewer(object):
    def setupUi(self, MapViewer):
        MapViewer.setObjectName("MapViewer")
        MapViewer.resize(475, 572)
        self.centralwidget = QtWidgets.QWidget(MapViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.show_date = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_date.sizePolicy().hasHeightForWidth())
        self.show_date.setSizePolicy(sizePolicy)
        self.show_date.setMaximumSize(QtCore.QSize(40, 20))
        self.show_date.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.show_date.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.show_date.setReadOnly(True)
        self.show_date.setOverwriteMode(False)
        self.show_date.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.show_date.setObjectName("show_date")
        self.gridLayout.addWidget(self.show_date, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.exit_QPush = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_QPush.sizePolicy().hasHeightForWidth())
        self.exit_QPush.setSizePolicy(sizePolicy)
        self.exit_QPush.setFlat(False)
        self.exit_QPush.setObjectName("exit_QPush")
        self.gridLayout.addWidget(self.exit_QPush, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.map_GLayout = QtWidgets.QGridLayout()
        self.map_GLayout.setObjectName("map_GLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 453, 390))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.map_GLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.map_GLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.move_left = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_left.sizePolicy().hasHeightForWidth())
        self.move_left.setSizePolicy(sizePolicy)
        self.move_left.setMaximumSize(QtCore.QSize(20, 16777215))
        self.move_left.setObjectName("move_left")
        self.horizontalLayout_2.addWidget(self.move_left)
        self.date_slider = QtWidgets.QSlider(self.centralwidget)
        self.date_slider.setOrientation(QtCore.Qt.Horizontal)
        self.date_slider.setObjectName("date_slider")
        self.horizontalLayout_2.addWidget(self.date_slider)
        self.move_right = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_right.sizePolicy().hasHeightForWidth())
        self.move_right.setSizePolicy(sizePolicy)
        self.move_right.setMinimumSize(QtCore.QSize(10, 0))
        self.move_right.setMaximumSize(QtCore.QSize(20, 16777215))
        self.move_right.setObjectName("move_right")
        self.horizontalLayout_2.addWidget(self.move_right)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.comboBox_map1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_map1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox_map1.setObjectName("comboBox_map1")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.setItemText(0, "")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.comboBox_map1.addItem("")
        self.gridLayout.addWidget(self.comboBox_map1, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_zoom = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_zoom.sizePolicy().hasHeightForWidth())
        self.pushButton_zoom.setSizePolicy(sizePolicy)
        self.pushButton_zoom.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_zoom.setObjectName("pushButton_zoom")
        self.gridLayout.addWidget(self.pushButton_zoom, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MapViewer.setCentralWidget(self.centralwidget)
        self.actionExport_ALl = QtWidgets.QAction(MapViewer)
        self.actionExport_ALl.setObjectName("actionExport_ALl")
        self.actionExit = QtWidgets.QAction(MapViewer)
        self.actionExit.setObjectName("actionExit")
        self.actionRoot = QtWidgets.QAction(MapViewer)
        self.actionRoot.setObjectName("actionRoot")

        self.retranslateUi(MapViewer)
        QtCore.QMetaObject.connectSlotsByName(MapViewer)

    def retranslateUi(self, MapViewer):
        _translate = QtCore.QCoreApplication.translate
        MapViewer.setWindowTitle(_translate("MapViewer", "MainWindow"))
        self.exit_QPush.setText(_translate("MapViewer", "Exit"))
        self.move_left.setText(_translate("MapViewer", "<"))
        self.move_right.setText(_translate("MapViewer", ">"))
        self.comboBox_map1.setItemText(1, _translate("MapViewer", "Change DOY"))
        self.comboBox_map1.setItemText(2, _translate("MapViewer", "Change Magnitude"))
        self.comboBox_map1.setItemText(3, _translate("MapViewer", "Change QA"))
        self.comboBox_map1.setItemText(4, _translate("MapViewer", "Segment Length"))
        self.comboBox_map1.setItemText(5, _translate("MapViewer", "Time Since Last Change"))
        self.comboBox_map1.setItemText(6, _translate("MapViewer", "Primary Land Cover"))
        self.comboBox_map1.setItemText(7, _translate("MapViewer", "Secondary Land Cover"))
        self.comboBox_map1.setItemText(8, _translate("MapViewer", "Primary Land Cover Confidence"))
        self.comboBox_map1.setItemText(9, _translate("MapViewer", "Secondary Land Cover Confidence"))
        self.pushButton_zoom.setText(_translate("MapViewer", "Zoom to Point"))
        self.actionExport_ALl.setText(_translate("MapViewer", "Export All"))
        self.actionExit.setText(_translate("MapViewer", "Exit"))
        self.actionRoot.setText(_translate("MapViewer", "Root"))
