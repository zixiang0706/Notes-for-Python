# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Thu Jul 25 21:17:46 2019
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page1)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.page1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.page1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.page1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.page1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.close_BT = QtWidgets.QPushButton(self.page1)
        self.close_BT.setObjectName("close_BT")
        self.horizontalLayout_2.addWidget(self.close_BT)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page1)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.gridLayout_2.addWidget(self.groupBox_2, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.page1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.page1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 9, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.page1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.page1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 11, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.dial = QtWidgets.QDial(self.page1)
        self.dial.setObjectName("dial")
        self.horizontalLayout_6.addWidget(self.dial)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 3, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lcdNumber = QtWidgets.QLCDNumber(self.page1)
        self.lcdNumber.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_5.addWidget(self.lcdNumber)
        self.horizontalSlider = QtWidgets.QSlider(self.page1)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalSlider.setMaximum(999)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 3, 1, 1)
        self.tabWidget.addTab(self.page1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 3, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMaximumSize(QtCore.QSize(100, 100))
        self.label_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("asset/andrew.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 4, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset/andrew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("asset/andrew.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuprojecr = QtWidgets.QMenu(self.menubar)
        self.menuprojecr.setObjectName("menuprojecr")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setIcon(icon)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setIcon(icon)
        self.actionclose.setObjectName("actionclose")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setIcon(icon)
        self.actionexit.setObjectName("actionexit")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setIcon(icon)
        self.actionnew.setObjectName("actionnew")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        self.actionpaste.setObjectName("actionpaste")
        self.actioncut = QtWidgets.QAction(MainWindow)
        self.actioncut.setObjectName("actioncut")
        self.actionopen_project = QtWidgets.QAction(MainWindow)
        self.actionopen_project.setObjectName("actionopen_project")
        self.actionexport_project = QtWidgets.QAction(MainWindow)
        self.actionexport_project.setObjectName("actionexport_project")
        self.actionclose_project = QtWidgets.QAction(MainWindow)
        self.actionclose_project.setObjectName("actionclose_project")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionregister = QtWidgets.QAction(MainWindow)
        self.actionregister.setObjectName("actionregister")
        self.actioncontact_us = QtWidgets.QAction(MainWindow)
        self.actioncontact_us.setObjectName("actioncontact_us")
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionclose)
        self.menufile.addAction(self.actionexit)
        self.menuedit.addAction(self.actioncopy)
        self.menuedit.addAction(self.actionpaste)
        self.menuedit.addAction(self.actioncut)
        self.menuprojecr.addAction(self.actionopen_project)
        self.menuprojecr.addAction(self.actionexport_project)
        self.menuprojecr.addAction(self.actionclose_project)
        self.menuhelp.addAction(self.actionhelp)
        self.menuhelp.addAction(self.actionregister)
        self.menuhelp.addAction(self.actioncontact_us)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuprojecr.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.close_BT, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我是andrew</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">typed by me</p></body></html>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "fullScreen", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "changText", None, -1))
        self.close_BT.setText(QtWidgets.QApplication.translate("MainWindow", "exit", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("MainWindow", "agree", None, -1))
        self.radioButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "neither", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "not agree", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.radioButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "name1", None, -1))
        self.radioButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "name2", None, -1))
        self.radioButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "name3", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "mess", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "about", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "input", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "user define dialog", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "dial num", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.page1), QtWidgets.QApplication.translate("MainWindow", "page1", None, -1))
        self.pushButton_10.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "page2", None, -1))
        self.menufile.setTitle(QtWidgets.QApplication.translate("MainWindow", "file", None, -1))
        self.menuedit.setTitle(QtWidgets.QApplication.translate("MainWindow", "edit", None, -1))
        self.menuprojecr.setTitle(QtWidgets.QApplication.translate("MainWindow", "projecr", None, -1))
        self.menuhelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "help", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.actionopen.setText(QtWidgets.QApplication.translate("MainWindow", "open", None, -1))
        self.actionclose.setText(QtWidgets.QApplication.translate("MainWindow", "close", None, -1))
        self.actionexit.setText(QtWidgets.QApplication.translate("MainWindow", "exit", None, -1))
        self.actionexit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Q", None, -1))
        self.actionnew.setText(QtWidgets.QApplication.translate("MainWindow", "new", None, -1))
        self.actioncopy.setText(QtWidgets.QApplication.translate("MainWindow", "copy", None, -1))
        self.actionpaste.setText(QtWidgets.QApplication.translate("MainWindow", "paste", None, -1))
        self.actioncut.setText(QtWidgets.QApplication.translate("MainWindow", "cut", None, -1))
        self.actionopen_project.setText(QtWidgets.QApplication.translate("MainWindow", "open project", None, -1))
        self.actionexport_project.setText(QtWidgets.QApplication.translate("MainWindow", "export project", None, -1))
        self.actionclose_project.setText(QtWidgets.QApplication.translate("MainWindow", "close project", None, -1))
        self.actionhelp.setText(QtWidgets.QApplication.translate("MainWindow", "help", None, -1))
        self.actionregister.setText(QtWidgets.QApplication.translate("MainWindow", "register", None, -1))
        self.actioncontact_us.setText(QtWidgets.QApplication.translate("MainWindow", "contact us", None, -1))
