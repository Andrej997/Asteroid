from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians

class Bullet(QLabel):
    kreni = pyqtSignal()

    #x i y su koordinate rakete, rotation je broj slike (1 - 72)
    def __init__(self, x, y, rotation, scene: QGraphicsScene):
        super().__init__()
        self.image = QPixmap("Images/bullet.png")
        t = QTransform().rotate(rotation)
        self.image = self.image.transformed(t)
        self.setPixmap(self.image)
        self.init_x = x
        self.init_y = y
        self.scene = scene
        self.xMovement = float(cos(radians(rotation)))
        self.yMovement = float(sin(radians(rotation)))
        self.scene.addWidget(self)
        self.kreni.connect(self.moveSelf)
        self.initBullet()
    
    def initBullet(self):
        self.move(self.init_x, self.init_y)

    def moveSelf(self):
        y = self.geometry().y()
        x = self.geometry().x()
        self.init_x = float(self.init_x).__add__(self.xMovement)
        self.init_y = float(self.init_y).__sub__(self.yMovement)
        #if y > -35 and y < 490 and x > 0 and x < 600:
        self.move(self.init_x, self.init_y)
       # else:
            #self.kreni.disconnect()
            #self.destroy()


    

