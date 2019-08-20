from PySide2 import QtWidgets, QtGui, QtCore
import mainwindow
import os, threading, time, queue


class Mythreading(threading.Thread):
    def __init__(self, func, args):
        super(Mythreading,self).__init__()
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = func.__name__
        self.res = None

    def getResult(self):
        return self.res

    def run(self):
        print("starting: {} at: {}".format(self.name,time.ctime()))
        self.res = self.func(*self.args)
        print("finished at:{}".format(time.ctime()))


class MyQtApp(mainwindow.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.my_os_path = os.getcwd()
        self.setMainTB_queue = queue.Queue()
        self.setupUi(self)
        self.read1_PB.clicked.connect(self.readSecondTB)

    def writeTB(self):
        while True:
            if  self.setMainTB_queue.qsize() != 0:
                self.main_TB.append(self.setMainTB_queue.get(1))
            else:
                self.main_TB.append("freedom")
            time.sleep(2)

    def readSecondTB(self):
        content = self.second_TB.toPlainText()
        self.setMainTB_queue.put(content)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    t = Mythreading(qt_app.writeTB,())
    t.setDaemon(True)
    t.start()
    qt_app.show()
    app.exec_()