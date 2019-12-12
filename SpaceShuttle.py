from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer
from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians
from Bullet import Bullet
from PauseWindow import *
import math

rocketsList = ['Images/rocketship.png', 'Images/rocketship (1).png', 'Images/rocketship (3).png', 'Images/rocketship (4).png', 'Images/rocketship (5).png', 'Images/rocketship (6).png', 'Images/rocketship (7).png', 'Images/rocketship (8).png', 'Images/rocketship (9).png', 'Images/rocketship (10).png', 'Images/rocketship (11).png', 'Images/rocketship (12).png', 'Images/rocketship (13).png', 'Images/rocketship (14).png', 'Images/rocketship (15).png', 'Images/rocketship (16).png', 'Images/rocketship (17).png', 'Images/rocketship (18).png', 'Images/rocketship (19).png', 'Images/rocketship (20).png', 'Images/rocketship (21).png', 'Images/rocketship (2).png', 'Images/rocketship (22).png', 'Images/rocketship (23).png', 'Images/rocketship (24).png', 'Images/rocketship (25).png', 'Images/rocketship (26).png', 'Images/rocketship (27).png', 'Images/rocketship (28).png', 'Images/rocketship (29).png', 'Images/rocketship (30).png', 'Images/rocketship (31).png', 'Images/rocketship (32).png', 'Images/rocketship (33).png', 'Images/rocketship (34).png', 'Images/rocketship (35).png', 'Images/rocketship (36).png', 'Images/rocketship (37).png', 'Images/rocketship (38).png', 'Images/rocketship (39).png', 'Images/rocketship (40).png', 'Images/rocketship (41).png', 'Images/rocketship (42).png', 'Images/rocketship (43).png', 'Images/rocketship (44).png', 'Images/rocketship (45).png', 'Images/rocketship (46).png', 'Images/rocketship (47).png', 'Images/rocketship (48).png', 'Images/rocketship (49).png', 'Images/rocketship (50).png', 'Images/rocketship (51).png', 'Images/rocketship (52).png', 'Images/rocketship (53).png', 'Images/rocketship (54).png', 'Images/rocketship (55).png', 'Images/rocketship (56).png', 'Images/rocketship (56).png', 'Images/rocketship (57).png', 'Images/rocketship (58).png', 'Images/rocketship (59).png', 'Images/rocketship (60).png', 'Images/rocketship (61).png', 'Images/rocketship (62).png', 'Images/rocketship (63).png', 'Images/rocketship (64).png', 'Images/rocketship (65).png', 'Images/rocketship (66).png', 'Images/rocketship (67).png', 'Images/rocketship (68).png', 'Images/rocketship (69).png', 'Images/rocketship (70).png', 'Images/rocketship (71).png']
i = 1
paused = 1
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
        self.meci = []
        self.setGeometry(270, 0, 600, 500)
        global rocketsList
        global i
        self.moveX = float(0)
        self.moveY = float(1)
        self.xFull = float(270)
        self.yFull = float(0) 
        self.angle = 90
        self.setMoverImage(rocketsList[i])
        self.timer = QBasicTimer()
        self.timer.start(30, self)
        self.scene = QGraphicsScene()
        self.pause = PauseWindow(self)

    def setMoverImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))


    def keyPressEvent(self, event):
        global rocketsList
        global i
        global paused
        if event.key() == QtCore.Qt.Key_Left:
            i = (i + 1) % 72
            self.setMoverImage(rocketsList[i])
            self.angle = self.angle + 5
            self.moveX = cos(radians(self.angle))
            self.moveY = sin(radians(self.angle))
        elif event.key() == QtCore.Qt.Key_Right:
            i = (i - 1) % 72
            self.angle = self.angle - 5
            self.setMoverImage(rocketsList[i])
            self.moveX = cos(radians(self.angle))
            self.moveY = sin(radians(self.angle))
        elif event.key() == QtCore.Qt.Key_Up:
            self.yFull = float(self.yFull).__sub__(self.moveY)
            self.xFull = float(self.xFull).__add__(self.moveX)
            #round(self.geometry().x(),2) + round(self.moveX,2)
            #round(self.geometry().y(),2) - round(self.moveY,2)
            print(self.xFull, self.yFull)
            if (math.floor(self.yFull) == -250) :
                self.yFull = (self.yFull * -1) - 1.0
            elif (math.floor(self.yFull) == 250) :
                self.yFull = (self.yFull * -1) + 1.0
            elif (math.floor(self.xFull) == -22) :
                self.xFull = 570
            elif (math.floor(self.xFull) == 571):
                self.xFull = -21.0
            self.move(self.xFull, self.yFull)
            # ovde treba za gas logika
        elif event.key() == QtCore.Qt.Key_Space:
            metak = Bullet(self.x(), self.y(), self.angle, self.scene)
            self.meci.append(metak)
        elif event.key() == QtCore.Qt.Key_Escape:
            self.pause.show()
        else:
            QtWidgets.QLabel.keyPressEvent(self, event)
        
    def timerEvent(self, a0: 'QTimerEvent'):
        if len(self.meci) > 0:
            for metak in self.meci:
                metak.kreni.emit()


