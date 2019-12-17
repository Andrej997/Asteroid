from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians
import sys
import math
import time

import  Server

i = 1
ast_0 = 0
tmp = []


class Asteroid(QMainWindow):
    def __init__(self, spaceShuttleWindow):
        super().__init__()
        Server.initialize()
        centralWidget = spaceShuttleWindow
        self.setGeometry(300, 150, 600, 500)
        self.setCentralWidget(centralWidget)
        label = QLabel(centralWidget)

        self.asteroid_0 = StartAsteroid(centralWidget)
        self.asteroid_0.setFocus()
        self.asteroid_0.name = "ast_0"

        self.asteroid_1 = StartAsteroid(centralWidget)
        self.asteroid_1.setFocus()

        self.asteroid_2 = StartAsteroid(centralWidget)
        self.asteroid_2.setFocus()




        self.initUI()

    def initUI(self):
        self.center()
        self.setWindowTitle('Asteroids')

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()


class StartAsteroid(QtWidgets.QLabel):
    def __init__(self, parent=None):

        super().__init__(parent)
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

    def setImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))

    def whileTrue(self):
        global i
        global ast_0
        global tmp
        global coordinatesOfRocketsss

        ast_0 += 1
        # if(numberObj == 3):
        # numberObj = 0
        ast_0 = ast_0 % 2
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
        bigImage = QPixmap(fullPath)
        #cropedImage = bigImage.scaled(80, 80, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        cropedImage = bigImage.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
       # cropedImage = bigImage.scaled(30, 30, Qt.IgnoreAspectRatio, Qt.FastTransformation)
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


        if (inttX == Server.rocket1xCoordinates):
            #ovde bi trebala logika da se proverava i x i y koordinate da li su se poklopile
            #alii to onda gleda samo taj 1 pixel, treba da vidimo da to nekako proveravamo za vise piksela jer je kamen tipa 20x20 px
            #i ovako radi samo kada mu se bax x koordinata
            #znaci trebalo bi ici if(inttX +- 20px == Server.rocket1xCoordinates and inttY +- 20px == Server.rokcet1yCoordinates)
            Server.isRocketDead()
            Server.rocket1IsDestroyed = 2
            print("Destroyed asteroid.")
            #self.hide()


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

