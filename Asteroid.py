from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians
import sys
import  threading
import math
import time

import  Server

i = 1
ast_0 = 0
tmp = []
levelOfAsteroid = 2
isDestroyedThisObj1 = 0

class Asteroid(QMainWindow):
    def __init__(self, spaceShuttleWindow):
        super().__init__()
        Server.initialize()
        centralWidget = spaceShuttleWindow
        self.setGeometry(300, 150, 600, 500)
        self.setFixedSize(600, 500)
        self.setCentralWidget(centralWidget)
        label = QLabel(centralWidget)

        self.asteroid_0 = StartAsteroid(centralWidget)
        self.asteroid_0.setFocus()
        self.asteroid_0.name = "ast_0"

        self.asteroid_1 = StartAsteroid(centralWidget)
        self.asteroid_1.setFocus()

        self.asteroid_2 = StartAsteroid(centralWidget)
        self.asteroid_2.setFocus()

        self.asteroid_3 = StartAsteroid(centralWidget)
        self.asteroid_3.setFocus()

        self.initUI()


    def set_status_bar(self):
        self.statusBar().setStyleSheet(
            "QStatusBar{background:rgba(0,0, 0,255);color:rgba(22,142,252,255);font-weight:bold; font-size:10;}")
        text = "LEVEL:1 \t\t|\t\tSCORE: PLAYER1-"+ Server.player1Score.__str__()  + "\t\t\t\tPLAYER2-"+ Server.player2Score.__str__()  + \
               "\t\t\t\tPLAYER3-"+ Server.player3Score.__str__()  + "\t\t\t\tPLAYER4-"+ Server.player4Score.__str__()  + "\t\t|\t\tLIFE: " + Server.player1Lives.__str__()
        self.statusBar().showMessage(text)

    def initUI(self):
        self.center()
        self.setWindowTitle('Asteroids')

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()


class StartAsteroid(QtWidgets.QLabel):
    _alive = []
    def __init__(self, parent=None):
        StartAsteroid._alive.append(self)
        super(StartAsteroid, self).__init__(parent)
        self.setGeometry(270, 0, 600, 500)
        global i

        self.name = "asd"
        self.moveX = float(0)
        self.moveY = float(1)
        self.xFull = float(270)
        self.yFull = float(0)
        self.angle = 90
        #self.setImage("Images/AsteroidsImg/large/c10004.png")
        self.timer = QBasicTimer()
        self.timer.start(30, self)
        self.scene = QGraphicsScene()
        #self.setAsteroidSize()

    def setImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))


    def setAssteroidSize(self, fullPath):
        global levelOfAsteroid
        bigImage = QPixmap(fullPath)
        if levelOfAsteroid == 3:
            cropedImage = bigImage.scaled(80, 80, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        elif levelOfAsteroid == 2:
            cropedImage = bigImage.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        else:
            cropedImage = bigImage.scaled(30, 30, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        return cropedImage

    def commit_suicide(self):
        self._alive.remove(self)

    def whileTrue(self):
        global i
        global ast_0
        global tmp
        global coordinatesOfRocketsss
        global levelOfAsteroid
        global isDestroyedThisObj1

        self.parent().parent().set_status_bar()
        ast_0 += 1
        # if(numberObj == 3):
        # numberObj = 0
        ast_0 = ast_0 % 4
#        print(ast_0)
        startPath = "Images/AsteroidsImg/large/c100"
        endPath = ".png"
        # if(numberObj % 2 == 0):
        #     i = (i - 1) % 16
        # else:
        i = (i + 1) % 16
        if i < 10:
            fullPath = (startPath + '0' + str(i) + endPath)
        else:
            fullPath = (startPath + str(i) + endPath)

        cropedImage = self.setAssteroidSize(fullPath)
        self.setImage(cropedImage)
        if (ast_0 % 2 == 0):
            self.angle = self.angle - ast_0
        else:
            self.angle = self.angle + ast_0



        self.moveX = cos(radians(self.angle))
        self.moveY = sin(radians(self.angle))
        self.yFull = float(self.yFull).__sub__(self.moveY * 9)
        self.xFull = float(self.xFull).__add__(self.moveX * 6)
        self.move(self.xFull, self.yFull)

        inttX = int(round(self.xFull))
        inttY = int(round(self.yFull))

        # region /logika da se asteroid gleda kao 20x20 px po x i y koordinati
        ccc = -10
        vvv = -10
        thisAsteroidXCoords = []
        thisAsteroidYCoords = []

        thisAsteroidXCoords.clear()
        thisAsteroidYCoords.clear()

        for ccc in range(20):
            tmpss = inttX + ccc
            thisAsteroidXCoords.append(tmpss)
            ccc = ccc + 1

        for vvv in range(20):
            tmpss2 = inttY + vvv
            thisAsteroidYCoords.append(tmpss2)
            vvv = vvv + 1

        if(any(checkXCords in thisAsteroidXCoords for checkXCords in Server.coordinatesOfRocketsX) and any(checkYCords in thisAsteroidYCoords for checkYCords in Server.coordinatesOfRocketsY)):
            #    Server.isRocketDead()
            #    Server.rocket1IsDestroyed = 2
            #    print("Destroyed asteroid.")
            #    #self.hide()
            #levelOfAsteroid = levelOfAsteroid -1
            Server.player1Lives = Server.player1Lives - 1
            self.hide()
            print("ASTEROID IS DESTROYED TOO!!!")
        #end region

        if (math.floor(self.yFull) <= -250):
            self.yFull = (self.yFull * -1) - 1.0
        elif (math.floor(self.yFull) >= 250):
            self.yFull = (self.yFull * -1) + 1.0
        elif (math.floor(self.xFull) <= -22):
            self.xFull = 559
        elif (math.floor(self.xFull) >= 560):
            self.xFull = -21.0
        # time.sleep(0.049)
        # time.sleep(0.039)
        # time.sleep(0.029)
        #time.sleep(0.019)
        time.sleep(0.007)
        #time.sleep(0.005)

    def timerEvent(self, a0: 'QTimerEvent'):
        self.whileTrue()

