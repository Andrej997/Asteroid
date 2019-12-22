from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians, floor
import server

class Bullet(QLabel):
    kreni = pyqtSignal()
    # x i y su koordinate rakete, rotation je broj slike (1 - 72)
    def __init__(self, x, y, rotation, i, scene: QGraphicsScene):
        super().__init__()
        self.image = QPixmap("Images/bullet.png")
        t = QTransform().rotate(rotation)
        self.setStyleSheet("background:transparent;color:white;")
        self.image = self.image.transformed(t)
        self.setPixmap(self.image)
        self.init_x = x + 20 + 30 * float(cos(radians(rotation)))
        self.init_y = y + 20 - 30 * float(sin(radians(rotation)))
        self.scene = scene
        self.xMovement = float(cos(radians(rotation)))
        self.yMovement = float(sin(radians(rotation)))
        scene.addWidget(self)
        self.kreni.connect(self.moveSelf)
        self.initBullet()

    def initBullet(self):
        self.move(self.init_x, self.init_y)
        self.show()

    def moveSelf(self):
        self.init_x = float(self.init_x).__add__(self.xMovement * 3)
        self.init_y = float(self.init_y).__sub__(self.yMovement * 3)
        if floor(self.init_x) <= - 22 or floor(self.init_x) >= 620 or floor(self.init_y) <= -250 or floor(
                self.init_y) >= 520:
            self.kreni.disconnect()
            self.destroy()
            self.hide()
        else:
            self.move(self.init_x, self.init_y)
            #server.metkoviCoordsX.append(self.init_x)logika za metkove
            #server.metkoviCoordsY.append(self.init_y)





