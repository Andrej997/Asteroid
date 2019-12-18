from SpaceShuttle import Mover
from Bullet import Bullet
import Asteroid
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGraphicsTransform
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF
from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from multiprocessing import Process

class GameMaker(QGraphicsView):
    def __init__(self, numberOfPlayers):
        super().__init__()
        self.w = 600
        self.h = 500
        self.rect().center()
        self.setFixedSize(self.w, self.h)
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(QRectF(0, -220, 590, 490))
        self.setScene(self.scene)
        self.labels = QLabel()
        self.pixmap = QPixmap('Images/img.png')
        self.labels.setPixmap(self.pixmap)
        self.labels.resize(600, 500)
        self.labels.move(-5,-225)
        self.scene.addWidget(self.labels)
        self.player1 = Mover(200, 0, 1)
        self.scene.addWidget(self.player1)
        if(numberOfPlayers == 2):
            self.player2 = Mover(300, 0, 2)
            self.scene.addWidget(self.player2)
        self.show()
        self.update()
        self.timer = QBasicTimer()
        self.timer.start(10, self)
    

    def keyPressEvent(self, event):
        if(event.key() == QtCore.Qt.Key_Left or event.key() == QtCore.Qt.Key_Up or event.key() == QtCore.Qt.Key_Right or event.key() == QtCore.Qt.Key_0):
            self.player1.KeyPressEvent1(event, self.scene)
        elif(event.key() == QtCore.Qt.Key_A or event.key() == QtCore.Qt.Key_D or event.key() == QtCore.Qt.Key_W or event.key() == QtCore.Qt.Key_G):
            self.player2.KeyPressEvent2(event, self.scene)
        
