from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform, QShortcut
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent, Qt
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform, QKeySequence
from math import cos, sin, radians
import  math
import random
import server
from game_over_scene import *
i = 1
ast_0 = 0
tmp = []
levelOfAsteroid = 2
isDestroyedThisObj1 = 0
tmpss = 0


class Asteroid(QLabel):
    def __init__(self, w, h, scene: QGraphicsScene, uniqueIdenfier):
        super().__init__()
        global i
        global tmpss
        self.size = 3
        self.am_i_alive = 0
        self.width = w
        self.height = h
        self.myScene = scene
        self.uniqueIdenfier = uniqueIdenfier
        self.moveX = float(0)
        self.moveY = float(1)
        self.xFull = float(float(random.randrange(0, 500)))#pocetne koordinate asteroida
        self.yFull = float(float(random.randrange(0, 450)))#pocetne koordinate asteroida
        tmpss = tmpss + 20
        self.angle = 90
        self.timer = QBasicTimer()
        self.timer.start(60, self)

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


    def whileTrue(self):
        global i
        global ast_0
        global tmp
        global coordinatesOfRocketsss
        global levelOfAsteroid
        global isDestroyedThisObj1
        if server.activeAsteroids[self.uniqueIdenfier] == 0:
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
            self.yFull = float(self.yFull).__sub__(self.moveY * 10)
            self.xFull = float(self.xFull).__add__(self.moveX * 5)
            self.move(self.xFull, self.yFull)

            #region unistavanje asteroida
            inttX = int(round(self.xFull))
            inttY = int(round(self.yFull))

            ccc = -10
            vvv = -10
            thisAsteroidXCoords = []
            thisAsteroidYCoords = []

            thisAsteroidXCoords.clear()
            thisAsteroidYCoords.clear()

            for ccc in range(40):
                tmpss = inttX + ccc
                thisAsteroidXCoords.append(tmpss)
                ccc = ccc + 1

            for vvv in range(40):
                tmpss2 = inttY + vvv
                thisAsteroidYCoords.append(tmpss2)
                vvv = vvv + 1

            if (any(checkXCords in thisAsteroidXCoords for checkXCords in server.coordinatesOfRocketsX) and any(
                    checkYCords in thisAsteroidYCoords for checkYCords in server.coordinatesOfRocketsY)):
                if server.player1Lives == 0:#ako je izgubio sve zivote da iskoci iz igrce
                    self.myScene.game_is_over()
                server.player1Lives = server.player1Lives - 1
                self.myScene.label2.setText("Player1 lives--->[" + server.player1Lives.__str__() + "] score--->[" + server.player1Score.__str__() + "]")
                server.activeAsteroids[self.uniqueIdenfier] = 1
                self.hide()
                print("ASTEROID IS DESTROYED TOO!!!")
            #endRegion

            #if(any(checkXCords in thisAsteroidXCoords for checkXCords in server.metkoviCoordsX) and any(
            #    checkYCords in thisAsteroidYCoords for checkYCords in server.metkoviCoordsY)):
            #    server.activeAsteroids[self.uniqueIdenfier] = 1
            #    self.hide()

            if (math.floor(self.yFull) <= -10):
                self.yFull = 500
            elif (math.floor(self.yFull) >= 500):
                self.yFull = 0
            elif (math.floor(self.xFull) <= -22):
                self.xFull = 559
            elif (math.floor(self.xFull) >= 600):
                self.xFull = -21.0
        else:
            self.yFull = 1000
            self.xFull = 1000

    def timerEvent(self, a0: 'QTimerEvent'):
        self.whileTrue()

