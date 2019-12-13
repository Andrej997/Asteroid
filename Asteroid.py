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

i = 1
ast_0 = 0


class Asteroid(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QtWidgets.QWidget()
        self.setGeometry(300, 150, 600, 500)
        self.setCentralWidget(centralWidget)
        # self.label = QLabel(centralWidget)
        # self.pixmap = QPixmap('Images/img.png')
        # self.label.setPixmap(self.pixmap)
        # self.label.resize(600, 500)
        label = QLabel(centralWidget)
        pixmap = QPixmap('Images/img.png')
        label.setPixmap(pixmap)
        label.resize(600, 500)
        # label.move(120, 160)

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
        self.setImage("Images/AsteroidsImg/small/a10000.png")
        self.timer = QBasicTimer()
        self.timer.start(30, self)
        self.scene = QGraphicsScene()

    def setImage(self, param):
        self.setPixmap(QtGui.QPixmap(param))

    def whileTrue(self):
        global i
        global ast_0
        ast_0 += 1
        # if(numberObj == 3):
        # numberObj = 0
        ast_0 = ast_0 % 4
        print(ast_0)
        startPath = "Images/AsteroidsImg/small/a100"
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
        # cropedImage = bigImage.scaled(80, 80, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        # cropedImage = bigImage.scaled(50, 50, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        cropedImage = bigImage.scaled(30, 30, Qt.IgnoreAspectRatio, Qt.FastTransformation)
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
        print(self.xFull, self.yFull)
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
        # time.sleep(0.019)
        # time.sleep(0.009)
        time.sleep(0.005)

    def timerEvent(self, a0: 'QTimerEvent'):
        self.whileTrue()



