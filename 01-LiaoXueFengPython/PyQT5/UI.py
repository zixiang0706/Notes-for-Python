#-*- coding:utf-8 -*-
'''
Basic Layout
'''
import sys,time
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import  QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit
import queue,threading
#https://blog.csdn.net/zhulove86/article/details/52563298


class TianGong(QWidget):
    def __init__(self):
        super(TianGong,self).__init__()
        self.setGeometry(300, 300, 700, 600)
        self.initUi()

    def initUi(self):
        self.createGridGroupBox()
        self.creatFormGroupBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Grid layout")
        layout = QGridLayout()

        lift_Label = QLabel("Lift")
        lift_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.lift_LineEdit = QLineEdit("...")
        group_Label = QLabel("Group")
        group_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.group_LineEdit = QLineEdit("...")
        building_Label = QLabel("Building")
        building_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.building_LineEdit = QLineEdit("...")
        floor_Label = QLabel("Floor")
        floor_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.floor_LineEdit = QLineEdit("...")
        value_Label = QLabel("Value")
        value_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.value_LineEdit = QLineEdit("...")
        servingDir_Label = QLabel("ServingDir")
        servingDir_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.servingDir_LineEdit = QLineEdit("...")
        destFloor_Label = QLabel("DestFloor")
        destFloor_Label.setFont(QFont("SansSerif", 14, QFont.Bold))
        self.destFloor_LineEdit = QLineEdit("...")
        imgeLabel = QLabel()
        pixMap = QPixmap("11.png")
        imgeLabel.setPixmap(pixMap)

        layout.setSpacing(10)
        layout.addWidget(lift_Label,0,0)
        layout.addWidget(self.lift_LineEdit,0,1)
        layout.addWidget(group_Label,1,0)
        layout.addWidget(self.group_LineEdit,1,1)
        layout.addWidget(building_Label,2,0)
        layout.addWidget(self.building_LineEdit,2,1)
        layout.addWidget(floor_Label, 3, 0)
        layout.addWidget(self.floor_LineEdit, 3, 1)
        layout.addWidget(value_Label, 4, 0)
        layout.addWidget(self.value_LineEdit, 4, 1)
        layout.addWidget(servingDir_Label, 5, 0)
        layout.addWidget(self.servingDir_LineEdit, 5, 1)
        layout.addWidget(destFloor_Label, 6, 0)
        layout.addWidget(self.destFloor_LineEdit, 6, 1)
        layout.addWidget(imgeLabel,0,2,7,1)
        layout.addWidget(imgeLabel, 0, 3, 7, 1)
        # layout.setColumnStretch(1, 10)
        self.gridGroupBox.setLayout(layout)
        self.setWindowTitle('Basic Layout')


    def creatFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        planLabel = QLabel("Log：")
        self.planEditor = QTextEdit()
        self.planEditor.setPlainText("===="*18)
        layout.addRow(planLabel,self.planEditor)
        self.formGroupBox.setLayout(layout)


    def updatePara(self,data_dict):
        self.planEditor.insertPlainText(str(data_dict) + '\n')
        for key,value in data_dict.items():
            if key == 'lift':
                self.lift_LineEdit.setText(str(value))
            elif key == 'group':
                self.group_LineEdit.setText(str(value))
            elif key == 'building':
                self.building_LineEdit.setText(str(value))
            elif key == 'floor':
                self.floor_LineEdit.setText(str(value))
            elif key == 'value':
                self.value_LineEdit.setText(str(value))
            elif key == 'servingDir':
                self.servingDir_LineEdit.setText(str(value))
            elif key == 'destFloor':
                self.destFloor_LineEdit.setText(str(value))

        QApplication.processEvents()

def update_q(q,ex):
    while True:
        data_dict=q.get()
        ex.updatePara(data_dict)
def main(q):
    app = QApplication(sys.argv)
    ex = TianGong()
    ex.show()
    t1=threading.Thread(target=update_q,args=(q,ex,))
    t1.start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    q=queue.Queue()
    app = QApplication(sys.argv)
    ex = TianGong()
    ex.show()
    sys.exit(app.exec_())
