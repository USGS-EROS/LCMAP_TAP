# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MAPS_VIEWER.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapViewer(object):
    def setupUi(self, MapViewer):
        MapViewer.setObjectName("MapViewer")
        MapViewer.resize(1084, 584)
        self.centralwidget = QtWidgets.QWidget(MapViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.map_GLayout = QtWidgets.QGridLayout()
        self.map_GLayout.setObjectName("map_GLayout")
        self.map2_QLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.map2_QLabel.sizePolicy().hasHeightForWidth())
        self.map2_QLabel.setSizePolicy(sizePolicy)
        self.map2_QLabel.setMinimumSize(QtCore.QSize(350, 350))
        self.map2_QLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.map2_QLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.map2_QLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.map2_QLabel.setText("")
        self.map2_QLabel.setObjectName("map2_QLabel")
        self.map_GLayout.addWidget(self.map2_QLabel, 0, 1, 1, 1)
        self.map3_QLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.map3_QLabel.sizePolicy().hasHeightForWidth())
        self.map3_QLabel.setSizePolicy(sizePolicy)
        self.map3_QLabel.setMinimumSize(QtCore.QSize(350, 350))
        self.map3_QLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.map3_QLabel.setSizeIncrement(QtCore.QSize(0, 0))
        self.map3_QLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.map3_QLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.map3_QLabel.setText("")
        self.map3_QLabel.setObjectName("map3_QLabel")
        self.map_GLayout.addWidget(self.map3_QLabel, 0, 2, 1, 1)
        self.map1_QLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.map1_QLabel.sizePolicy().hasHeightForWidth())
        self.map1_QLabel.setSizePolicy(sizePolicy)
        self.map1_QLabel.setMinimumSize(QtCore.QSize(350, 350))
        self.map1_QLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.map1_QLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.map1_QLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.map1_QLabel.setText("")
        self.map1_QLabel.setObjectName("map1_QLabel")
        self.map_GLayout.addWidget(self.map1_QLabel, 0, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.exit_QPush = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_QPush.sizePolicy().hasHeightForWidth())
        self.exit_QPush.setSizePolicy(sizePolicy)
        self.exit_QPush.setFlat(False)
        self.exit_QPush.setObjectName("exit_QPush")
        self.gridLayout.addWidget(self.exit_QPush, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
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
        self.gridLayout.addWidget(self.show_date, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_map1 = QtWidgets.QComboBox(self.centralwidget)
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
        self.verticalLayout_2.addWidget(self.comboBox_map1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_map2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_map2.setObjectName("comboBox_map2")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.setItemText(0, "")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.comboBox_map2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_map2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_map3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_map3.setObjectName("comboBox_map3")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.setItemText(0, "")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.comboBox_map3.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_map3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        MapViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MapViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MapViewer)
        self.statusbar.setObjectName("statusbar")
        MapViewer.setStatusBar(self.statusbar)
        self.actionExport_ALl = QtWidgets.QAction(MapViewer)
        self.actionExport_ALl.setObjectName("actionExport_ALl")
        self.actionExit = QtWidgets.QAction(MapViewer)
        self.actionExit.setObjectName("actionExit")
        self.actionRoot = QtWidgets.QAction(MapViewer)
        self.actionRoot.setObjectName("actionRoot")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_ALl)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MapViewer)
        QtCore.QMetaObject.connectSlotsByName(MapViewer)

    def retranslateUi(self, MapViewer):
        _translate = QtCore.QCoreApplication.translate
        MapViewer.setWindowTitle(_translate("MapViewer", "MainWindow"))
        self.move_left.setText(_translate("MapViewer", "<"))
        self.move_right.setText(_translate("MapViewer", ">"))
        self.exit_QPush.setText(_translate("MapViewer", "Exit"))
        self.comboBox_map1.setItemText(1, _translate("MapViewer", "Change DOY"))
        self.comboBox_map1.setItemText(2, _translate("MapViewer", "Change Magnitude"))
        self.comboBox_map1.setItemText(3, _translate("MapViewer", "Change QA"))
        self.comboBox_map1.setItemText(4, _translate("MapViewer", "Segment Length"))
        self.comboBox_map1.setItemText(5, _translate("MapViewer", "Time Since Last Change"))
        self.comboBox_map1.setItemText(6, _translate("MapViewer", "Primary Land Cover"))
        self.comboBox_map1.setItemText(7, _translate("MapViewer", "Secondary Land Cover"))
        self.comboBox_map1.setItemText(8, _translate("MapViewer", "Primary Land Cover Confidence"))
        self.comboBox_map1.setItemText(9, _translate("MapViewer", "Secondary Land Cover Confidence"))
        self.comboBox_map2.setItemText(1, _translate("MapViewer", "Change DOY"))
        self.comboBox_map2.setItemText(2, _translate("MapViewer", "Change Magnitude"))
        self.comboBox_map2.setItemText(3, _translate("MapViewer", "Change QA"))
        self.comboBox_map2.setItemText(4, _translate("MapViewer", "Segment Length"))
        self.comboBox_map2.setItemText(5, _translate("MapViewer", "Time Since Last Change"))
        self.comboBox_map2.setItemText(6, _translate("MapViewer", "Primary Land Cover"))
        self.comboBox_map2.setItemText(7, _translate("MapViewer", "Secondary Land Cover"))
        self.comboBox_map2.setItemText(8, _translate("MapViewer", "Primary Land Cover Confidence"))
        self.comboBox_map2.setItemText(9, _translate("MapViewer", "Secondary Land Cover Confidence"))
        self.comboBox_map3.setItemText(1, _translate("MapViewer", "Change DOY"))
        self.comboBox_map3.setItemText(2, _translate("MapViewer", "Change Magnitude"))
        self.comboBox_map3.setItemText(3, _translate("MapViewer", "Change QA"))
        self.comboBox_map3.setItemText(4, _translate("MapViewer", "Segment Length"))
        self.comboBox_map3.setItemText(5, _translate("MapViewer", "Time Since Last Change"))
        self.comboBox_map3.setItemText(6, _translate("MapViewer", "Primary Land Cover"))
        self.comboBox_map3.setItemText(7, _translate("MapViewer", "Secondary Land Cover"))
        self.comboBox_map3.setItemText(8, _translate("MapViewer", "Primary Land Cover Confidence"))
        self.comboBox_map3.setItemText(9, _translate("MapViewer", "Secondary Land Cover Confidence"))
        self.menuFile.setTitle(_translate("MapViewer", "File"))
        self.actionExport_ALl.setText(_translate("MapViewer", "Export All"))
        self.actionExit.setText(_translate("MapViewer", "Exit"))
        self.actionRoot.setText(_translate("MapViewer", "Root"))
