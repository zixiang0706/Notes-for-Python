from PySide2 import QtWidgets
import mainwindow, dialog


class Dialog(dialog.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        self.setupUi(self)
        self.toolButton_2.clicked.connect(self.age)

    def age(self):
        answer, status = QtWidgets.QInputDialog.getInt(self,'title','hint',28, 1, 120)
        self.lineEdit_2.setText(str(answer))




class MyQtApp(mainwindow.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        # self.showMaximized()
        self.setWindowTitle("new title")
        self.pushButton_2.clicked.connect(self.changeText)
        self.radioButton_2.clicked.connect(self.radioChecked)
        self.dial.valueChanged[int].connect(self.dialChange)
        self.horizontalSlider.valueChanged[int].connect(self.sliderChange)


        self.pushButton_3.clicked.connect(self.mess)
        self.pushButton_4.clicked.connect(self.about)

        self.pushButton_6.clicked.connect(self.dialog)
        self.pushButton_5.clicked.connect(self.user_dialog)


    def changeText(self,e):
        self.label_2.setText('aaa')
        # self.textBrowser.append("hello world!")
        # self.textBrowser.setText("aaaa")
        print(self.textBrowser.toPlainText())

    def radioChecked(self):
        if self.radioButton_2.isChecked()== True:
            self.radioButton_6.setChecked(True)

    def dialChange(self,num):
        self.label_4.setText(str(num))

    def sliderChange(self,num):
        self.lcdNumber.display(num)

    def mess(self):
        QtWidgets.QMessageBox.information(self, 'info', u'show you some information')
        answer = QtWidgets.QMessageBox.question(self, 'info', u'show you some information')
        print(answer)
        if answer ==16384:
            print(111)
        answer = QtWidgets.QMessageBox.warning(self, 'info', u'show you some information')
        print(answer)
        answer = QtWidgets.QMessageBox.critical(self, 'info', u'show you some information')
        print(answer)

    def about(self):
        answer = QtWidgets.QMessageBox.about(self, 'info', u'show you some information\n'
                                                           u'this is meaningful')
        print(answer)
        answer = QtWidgets.QMessageBox.aboutQt(self)
        print(answer)

    def dialog(self):
        answer1,answer2 = QtWidgets.QInputDialog.getText(self, 'title', 'explain')
        print(answer1,answer2)

        answer1,answer2 = QtWidgets.QInputDialog.getInt(self, 'title', 'explain',30,0,200)
        print(answer1,answer2)

        ls = ['a', 'b', 'c', 'd']
        answer1,answer2 = QtWidgets.QInputDialog.getItem(self, 'title', 'explain', ls)
        print(answer1,answer2)

    def user_dialog(self):
        self.user_dialog_app = Dialog()
        self.user_dialog_app.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()