# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SYMBOLOGY.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_symbology(object):
    def setupUi(self, MainWindow_symbology):
        MainWindow_symbology.setObjectName("MainWindow_symbology")
        MainWindow_symbology.resize(280, 161)
        self.centralwidget = QtWidgets.QWidget(MainWindow_symbology)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_menus = QtWidgets.QGridLayout()
        self.gridLayout_menus.setObjectName("gridLayout_menus")
        self.label_color = QtWidgets.QLabel(self.centralwidget)
        self.label_color.setObjectName("label_color")
        self.gridLayout_menus.addWidget(self.label_color, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_marker = QtWidgets.QLabel(self.centralwidget)
        self.label_marker.setObjectName("label_marker")
        self.gridLayout_menus.addWidget(self.label_marker, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setObjectName("label_size")
        self.gridLayout_menus.addWidget(self.label_size, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.comboBox_marker = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_marker.setObjectName("comboBox_marker")
        self.gridLayout_menus.addWidget(self.comboBox_marker, 1, 0, 1, 1)
        self.comboBox_size = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_size.setObjectName("comboBox_size")
        self.gridLayout_menus.addWidget(self.comboBox_size, 1, 1, 1, 1)
        self.comboBox_color = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_color.setObjectName("comboBox_color")
        self.gridLayout_menus.addWidget(self.comboBox_color, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_menus)
        self.horizontalLayout_controls = QtWidgets.QHBoxLayout()
        self.horizontalLayout_controls.setObjectName("horizontalLayout_controls")
        self.pushButton_preview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.horizontalLayout_controls.addWidget(self.pushButton_preview)
        self.pushButton_apply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout_controls.addWidget(self.pushButton_apply)
        self.verticalLayout.addLayout(self.horizontalLayout_controls)
        self.horizontalLayout_preview = QtWidgets.QHBoxLayout()
        self.horizontalLayout_preview.setObjectName("horizontalLayout_preview")
        self.verticalLayout.addLayout(self.horizontalLayout_preview)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow_symbology.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_symbology)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow_symbology.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_symbology)
        self.statusbar.setObjectName("statusbar")
        MainWindow_symbology.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow_symbology)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow_symbology)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow_symbology)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_symbology)

    def retranslateUi(self, MainWindow_symbology):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_symbology.setWindowTitle(_translate("MainWindow_symbology", "Select Symbology"))
        self.label_color.setText(_translate("MainWindow_symbology", "Color"))
        self.label_marker.setText(_translate("MainWindow_symbology", "Marker"))
        self.label_size.setText(_translate("MainWindow_symbology", "Size"))
        self.pushButton_preview.setText(_translate("MainWindow_symbology", "Preview"))
        self.pushButton_apply.setText(_translate("MainWindow_symbology", "Apply"))
        self.menuFile.setTitle(_translate("MainWindow_symbology", "File"))
        self.actionLoad.setText(_translate("MainWindow_symbology", "Load"))
        self.actionSave.setText(_translate("MainWindow_symbology", "Save"))

