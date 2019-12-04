from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QTransform
import sys

rocketsList = ['Images/rocketship.png', 'Images/rocketship (1).png', 'Images/rocketship (3).png', 'Images/rocketship (4).png', 'Images/rocketship (5).png', 'Images/rocketship (6).png', 'Images/rocketship (7).png', 'Images/rocketship (8).png', 'Images/rocketship (9).png', 'Images/rocketship (10).png', 'Images/rocketship (11).png', 'Images/rocketship (12).png', 'Images/rocketship (13).png', 'Images/rocketship (14).png', 'Images/rocketship (15).png', 'Images/rocketship (16).png', 'Images/rocketship (17).png', 'Images/rocketship (18).png', 'Images/rocketship (19).png', 'Images/rocketship (20).png', 'Images/rocketship (21).png', 'Images/rocketship (2).png', 'Images/rocketship (22).png', 'Images/rocketship (23).png', 'Images/rocketship (24).png', 'Images/rocketship (25).png', 'Images/rocketship (26).png', 'Images/rocketship (27).png', 'Images/rocketship (28).png', 'Images/rocketship (29).png', 'Images/rocketship (30).png', 'Images/rocketship (31).png', 'Images/rocketship (32).png', 'Images/rocketship (33).png', 'Images/rocketship (34).png', 'Images/rocketship (35).png', 'Images/rocketship (36).png', 'Images/rocketship (37).png', 'Images/rocketship (38).png', 'Images/rocketship (39).png', 'Images/rocketship (40).png', 'Images/rocketship (41).png', 'Images/rocketship (42).png', 'Images/rocketship (43).png', 'Images/rocketship (44).png', 'Images/rocketship (45).png', 'Images/rocketship (46).png', 'Images/rocketship (47).png', 'Images/rocketship (48).png', 'Images/rocketship (49).png', 'Images/rocketship (50).png', 'Images/rocketship (51).png', 'Images/rocketship (52).png', 'Images/rocketship (53).png', 'Images/rocketship (54).png', 'Images/rocketship (55).png', 'Images/rocketship (56).png', 'Images/rocketship (56).png', 'Images/rocketship (57).png', 'Images/rocketship (58).png', 'Images/rocketship (59).png', 'Images/rocketship (60).png', 'Images/rocketship (61).png', 'Images/rocketship (62).png', 'Images/rocketship (63).png', 'Images/rocketship (64).png', 'Images/rocketship (65).png', 'Images/rocketship (66).png', 'Images/rocketship (67).png', 'Images/rocketship (68).png', 'Images/rocketship (69).png', 'Images/rocketship (70).png', 'Images/rocketship (71).png']
i = 54

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
        global rocketsList
        global i
        self.setMoverImage(rocketsList[i])

    def setMoverImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))


    def keyPressEvent(self, event):
        global rocketsList
        global i
        if event.key() == QtCore.Qt.Key_Up:
            i = (i + 1) % 72
            self.setMoverImage(rocketsList[i])

        elif event.key() == QtCore.Qt.Key_Down:
            i = (i - 1) % 72
            self.setMoverImage(rocketsList[i])

        elif event.key() == QtCore.Qt.Key_Q:
            self.move(self.x() + 5, self.y())
            # ovde treba za gas logika
        else:
            QtWidgets.QLabel.keyPressEvent(self, event)



