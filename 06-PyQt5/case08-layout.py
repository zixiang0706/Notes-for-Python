# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QApplication
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         lbl1 = QLabel('Zetcode', self)
#         lbl1.move(15, 10)
#
#         lbl2 = QLabel('tutorials', self)
#         lbl2.move(35, 40)
#
#         lbl3 = QLabel('for programmers', self)
#         lbl3.move(55, 70)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Absolute')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton,
#     QHBoxLayout, QVBoxLayout, QApplication)
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#         hbox.addStretch(1)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#         vbox.addStretch(1)
#
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Buttons')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())





# import sys
# from PyQt5.QtWidgets import (QWidget, QGridLayout,
#     QPushButton, QApplication)
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         grid = QGridLayout()
#         self.setLayout(grid)
#
#         names = ['Cls', 'Bck', '', 'Close',
#                  '7', '8', '9', '/',
#                 '4', '5', '6', '*',
#                  '1', '2', '3', '-',
#                 '0', '.', '=', '+']
#
#         positions = [(i,j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#
#             if name == '':
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button, *position)
#
#         self.move(300, 150)
#         self.setWindowTitle('Calculator')
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())




import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.initUI()



    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        print(self.count)
        self.count += 1


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
