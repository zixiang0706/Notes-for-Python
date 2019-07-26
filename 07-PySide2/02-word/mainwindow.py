# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Thu Jul 25 22:37:40 2019
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.read_PB = QtWidgets.QPushButton(self.frame)
        self.read_PB.setGeometry(QtCore.QRect(140, 340, 113, 32))
        self.read_PB.setObjectName("read_PB")
        self.write_PB = QtWidgets.QPushButton(self.frame)
        self.write_PB.setGeometry(QtCore.QRect(420, 340, 113, 32))
        self.write_PB.setObjectName("write_PB")
        self.write_PTE = QtWidgets.QPlainTextEdit(self.frame)
        self.write_PTE.setGeometry(QtCore.QRect(350, 140, 261, 191))
        self.write_PTE.setObjectName("write_PTE")
        self.read_TB = QtWidgets.QTextBrowser(self.frame)
        self.read_TB.setGeometry(QtCore.QRect(70, 140, 256, 192))
        self.read_TB.setObjectName("read_TB")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.read_PB.setText(QtWidgets.QApplication.translate("MainWindow", "read", None, -1))
        self.write_PB.setText(QtWidgets.QApplication.translate("MainWindow", "write", None, -1))
        self.menufile.setTitle(QtWidgets.QApplication.translate("MainWindow", "file", None, -1))
        self.actionsave.setText(QtWidgets.QApplication.translate("MainWindow", "save", None, -1))
        self.actionopen.setText(QtWidgets.QApplication.translate("MainWindow", "open", None, -1))

