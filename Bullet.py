from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians

class Bullet(QLabel):
    kreni = pyqtSignal()

    #x i y su koordinate rakete, rotation je broj slike (1 - 72)
    def __init__(self, x, y, rotation, scene: QGraphicsScene):
        super.__init__()
        image = QPixmap("Images/bullet.png")
        t = QTransform(rotation)
        rotatedImage = QPixmap.transformed(t)
        self.setPixmap(rotatedImage)
        self.init_x = x
        self.init_y = y
        self.scene = scene
        self.xMovement = cos(radians(rotation))
        self.yMovement = sin(radians(rotation))
        scene.addWidget(self)
        self.kreni.connect(self.moveSelf)
        self.initBullet()
    
    def initBullet(self):
        self.move(self.init_x + 5, self.init_y - 10)

    def moveSelf(self):
        y = self.geometry().y()
        x = self.geometry().x()
        if y > -35 and y < 490 and x > 0 and x < 600:
            self.move(self.geometry().x() + self.xMovement, self.geometry().y() - self.yMovement)
        else:
            self.kreni.disconnect()
            self.destroy()


    

