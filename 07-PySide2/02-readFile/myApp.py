from PySide2 import QtWidgets, QtGui, QtCore
import mainwindow
import os




class MyQtApp(mainwindow.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.my_os_path = os.getcwd()
        self.setupUi(self)
        self.read_PB.clicked.connect(self.my_read_BT)
        self.actionopen.triggered.connect(self.my_read_BT)

        self.write_PB.clicked.connect(self.my_write_BT)

    def my_read_BT(self):
        print('read button pressed')
        my_file_path = QtWidgets.QFileDialog.getOpenFileName(self,"open file",self.my_os_path)
        print(my_file_path)
        with open(my_file_path[0],'r') as f:
            self.read_TB.setPlainText(f.read())
            self.read_TB.append("\nfinished!")
        print('read info done')

    def my_write_BT(self):
        print("write button is pressed")
        my_file_path = QtWidgets.QFileDialog.getSaveFileName(self,"save file", self.my_os_path)
        print(my_file_path)
        if my_file_path[0]:
            with open(my_file_path[0], 'w') as f:
                f.write(self.write_PTE.toPlainText())
            print('write done')



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    # splash = QtWidgets.QSplashScreen(QtGui.QPixmap('asset/andrew.png'))
    # splash.show()
    # splash.showMessage("loading1 ...",QtCore.Qt.AlignCenter,QtCore.Qt.red)
    # app.processEvents()
    qt_app = MyQtApp()
    qt_app.show()
    # splash.finish(qt_app)
    app.exec_()