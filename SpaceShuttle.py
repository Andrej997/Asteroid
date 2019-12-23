from datetime import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent
import  math
from Bullet import *
import Server

rocketsList = ['Images/rocketship.png', 'Images/rocketship (1).png', 'Images/rocketship (3).png',
               'Images/rocketship (4).png', 'Images/rocketship (5).png', 'Images/rocketship (6).png',
               'Images/rocketship (7).png', 'Images/rocketship (8).png', 'Images/rocketship (9).png',
               'Images/rocketship (10).png', 'Images/rocketship (11).png', 'Images/rocketship (12).png',
               'Images/rocketship (13).png', 'Images/rocketship (14).png', 'Images/rocketship (15).png',
               'Images/rocketship (16).png', 'Images/rocketship (17).png', 'Images/rocketship (18).png',
               'Images/rocketship (19).png', 'Images/rocketship (20).png', 'Images/rocketship (21).png',
               'Images/rocketship (2).png', 'Images/rocketship (22).png', 'Images/rocketship (23).png',
               'Images/rocketship (24).png', 'Images/rocketship (25).png', 'Images/rocketship (26).png',
               'Images/rocketship (27).png', 'Images/rocketship (28).png', 'Images/rocketship (29).png',
               'Images/rocketship (30).png', 'Images/rocketship (31).png', 'Images/rocketship (32).png',
               'Images/rocketship (33).png', 'Images/rocketship (34).png', 'Images/rocketship (35).png',
               'Images/rocketship (36).png', 'Images/rocketship (37).png', 'Images/rocketship (38).png',
               'Images/rocketship (39).png', 'Images/rocketship (40).png', 'Images/rocketship (41).png',
               'Images/rocketship (42).png', 'Images/rocketship (43).png', 'Images/rocketship (44).png',
               'Images/rocketship (45).png', 'Images/rocketship (46).png', 'Images/rocketship (47).png',
               'Images/rocketship (48).png', 'Images/rocketship (49).png', 'Images/rocketship (50).png',
               'Images/rocketship (51).png', 'Images/rocketship (52).png', 'Images/rocketship (53).png',
               'Images/rocketship (54).png', 'Images/rocketship (55).png', 'Images/rocketship (56).png',
               'Images/rocketship (56).png', 'Images/rocketship (57).png', 'Images/rocketship (58).png',
               'Images/rocketship (59).png', 'Images/rocketship (60).png', 'Images/rocketship (61).png',
               'Images/rocketship (62).png', 'Images/rocketship (63).png', 'Images/rocketship (64).png',
               'Images/rocketship (65).png', 'Images/rocketship (66).png', 'Images/rocketship (67).png',
               'Images/rocketship (68).png', 'Images/rocketship (69).png', 'Images/rocketship (70).png',
               'Images/rocketship (71).png']

i = 1#rocket1 angle
i2 = 1 #rocket2 angle


class SpaceShuttle(QLabel):
    upRocket1 = pyqtSignal()
    fireRocket1 = pyqtSignal()
    leftRocket1 = pyqtSignal()
    rightRocket1 = pyqtSignal()
    upRocket2 = pyqtSignal()
    fireRocket2 = pyqtSignal()
    leftRocket2 = pyqtSignal()
    rightRocket2 = pyqtSignal()
    def __init__(self, w, h, scene: QGraphicsScene, num):
        super().__init__()
        self.meci = []
        self.width = w
        self.height = h
        self.myScene = scene
        self.numJMBG = num
        self.setPixmap(QtGui.QPixmap('Images/rocketship.png'))
        self.moveX = float(0)
        self.moveY = float(1)
        self.xFull = float(270)
        self.yFull = float(200)
        self.angle = 90
        self.move(270, 200)
        #region inizilatioin of signals for rocket1 and rocket2
        self.upRocket1.connect(self.up1_function)
        self.leftRocket1.connect(self.left1_function)
        self.rightRocket1.connect(self.right1_function)
        self.fireRocket1.connect(self.fire1_function)
        self.upRocket2.connect(self.up2_function)
        self.leftRocket2.connect(self.left2_function)
        self.rightRocket2.connect(self.right2_function)
        self.fireRocket2.connect(self.fire2_function)
        #endregion
        self.timer = QBasicTimer()
        self.timer.start(30, self)

    def setRocketImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))


    def positionsExpand(self):
        current_x_coords = int(round(self.x()))
        current_y_coords = int(round(self.y()))

        Server.coordinatesOfRocketsX.clear()
        Server.coordinatesOfRocketsY.clear()

        # region ->logika da se raketa gleda kao 20x20 px po x i y koordinati
        tmp = 0
        for tmpX1 in range(20):
            tmp = tmpX1 + current_x_coords
            Server.coordinatesOfRocketsX.append(tmp)
            tmpX1 = tmpX1 + 1
        tmp = 0
        for tmpX2 in range(20):
            tmp = current_x_coords - tmpX2
            Server.coordinatesOfRocketsX.append(tmp)
            tmpX2 = tmpX2 + 1
        tmp = 0
        for tmpY1 in range(20):
            tmp = tmpY1 + current_y_coords
            Server.coordinatesOfRocketsY.append(tmp)
            tmpY1 = tmpY1 + 1
        tmp = 0
        for tmpY2 in range(20):
            tmp = current_y_coords - tmpY2
            Server.coordinatesOfRocketsY.append(tmp)
            tmpY2 = tmpY2 + 1
        # end region

    def up1_function(self):
        global  i
        self.positionsExpand()
        self.yFull = float(self.yFull).__sub__(self.moveY * 4)
        self.xFull = float(self.xFull).__add__(self.moveX * 4)
        self.move(self.xFull, self.yFull)
        if (math.floor(self.yFull) <= -20):
            self.yFull = 500
        elif (math.floor(self.yFull) >= 500):
            self.yFull = 0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        self.update()

    def up2_function(self):
        global i2
        self.yFull = float(self.yFull).__sub__(self.moveY * 8)
        self.xFull = float(self.xFull).__add__(self.moveX * 8)
        self.move(self.xFull, self.yFull)
        if (math.floor(self.yFull) <= -20):
            self.yFull = 500
        elif (math.floor(self.yFull) >= 500):
            self.yFull = 0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        self.update()

    def left1_function(self):
        global i
        self.positionsExpand()

        i = (i + 1) % 72
        self.setRocketImage(rocketsList[i])
        self.angle = self.angle + 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def right1_function(self):
        global i
        self.positionsExpand()
        i = (i - 1) % 72
        self.angle = self.angle - 5
        self.setRocketImage(rocketsList[i])
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def fire1_function(self):
        global i
        self.positionsExpand()
        metak = Bullet(self.x(), self.y(), self.angle, i, self.myScene)
        self.meci.append(metak)
        self.update()

    def left2_function(self):
        global i2
        self.positionsExpand()
        i2 = (i2 + 1) % 72
        self.setRocketImage(rocketsList[i2])
        self.angle = self.angle + 5
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def right2_function(self):
        global i2
        self.positionsExpand()
        i2 = (i2 - 1) % 72
        self.angle = self.angle - 5
        self.setRocketImage(rocketsList[i2])
        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.update()

    def fire2_function(self):
        global i2
        self.positionsExpand()
        metak = Bullet(self.x(), self.y(), self.angle, i2, self.myScene)
        self.meci.append(metak)
        self.update()


    def timerEvent(self, a0: 'QTimerEvent'):
        if len(self.meci) > 0:
            for metak in self.meci:
                metak.kreni.emit()
