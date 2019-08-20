# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sat Jul 27 14:42:36 2019
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.read2_PB = QtWidgets.QPushButton(self.frame)
        self.read2_PB.setObjectName("read2_PB")
        self.gridLayout_2.addWidget(self.read2_PB, 3, 2, 1, 1)
        self.main_TB = QtWidgets.QTextBrowser(self.frame)
        self.main_TB.setObjectName("main_TB")
        self.gridLayout_2.addWidget(self.main_TB, 0, 0, 1, 1)
        self.read1_PB = QtWidgets.QPushButton(self.frame)
        self.read1_PB.setObjectName("read1_PB")
        self.gridLayout_2.addWidget(self.read1_PB, 2, 2, 1, 1)
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setObjectName("exit")
        self.gridLayout_2.addWidget(self.exit, 5, 2, 1, 1)
        self.read3_PB = QtWidgets.QPushButton(self.frame)
        self.read3_PB.setObjectName("read3_PB")
        self.gridLayout_2.addWidget(self.read3_PB, 4, 2, 1, 1)
        self.second_TB = QtWidgets.QTextBrowser(self.frame)
        self.second_TB.setReadOnly(False)
        self.second_TB.setObjectName("second_TB")
        self.gridLayout_2.addWidget(self.second_TB, 2, 0, 4, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exit, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.read2_PB.setText(QtWidgets.QApplication.translate("MainWindow", "read2", None, -1))
        self.read1_PB.setText(QtWidgets.QApplication.translate("MainWindow", "read1", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("MainWindow", "exit", None, -1))
        self.read3_PB.setText(QtWidgets.QApplication.translate("MainWindow", "read3", None, -1))

