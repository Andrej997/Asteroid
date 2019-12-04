from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QTransform
import sys


class SpaceShuttle(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QtWidgets.QWidget()
        self.setGeometry(300, 150, 600, 500)
        self.setCentralWidget(centralWidget)
        self.mover = Mover(centralWidget)
        self.mover.setFocus()
        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('Asteroids')
        #self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()

class Mover(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(270, 0, 600, 500)
        self.setPixmap(QtGui.QPixmap('Images/rocketship.png'))


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.move(self.x(), self.y() - 5)
        elif event.key() == QtCore.Qt.Key_Down:
            self.move(self.x(), self.y() + 5)
        elif event.key() == QtCore.Qt.Key_Left:
            self.move(self.x() - 5, self.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.move(self.x() + 5, self.y())
        else:
            QtWidgets.QLabel.keyPressEvent(self, event)



