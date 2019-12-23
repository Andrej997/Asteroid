from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QGraphicsScene
from PyQt5.QtGui import QPixmap, QTransform
from math import cos, sin, radians, floor
import Server

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
        self.IDS = Server.bulletIDS
        Server.bulletIDS = Server.bulletIDS + 1
        inttX = int(round(self.init_x))
        inttY = int(round(self.init_y))
        Server.bulletsCollectionX[self.IDS] = 0
        Server.bulletsCollectionY[self.IDS] = 0
        Server.bulletsCollectionX[self.IDS] = inttX
        Server.bulletsCollectionY[self.IDS] = inttY

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
        if floor(self.init_x) <= -50 or floor(self.init_x) >= 603 or floor(self.init_y) <= -50 or floor(#vece dimenzije za metak jer bagguje nestoo ako se samnje , tj bug je u tome da se fakticki puca van scene
                self.init_y) >= 555:
            Server.bulletsCollectionX[self.IDS] = 99999
            Server.bulletsCollectionY[self.IDS] = 99999
            self.kreni.disconnect()
            self.destroy()
            self.hide()
        else:
            self.move(self.init_x, self.init_y)
            inttXXX = int(round(self.init_x))
            inttYYY = int(round(self.init_y))
            Server.bulletsCollectionX[self.IDS] = inttXXX
            Server.bulletsCollectionY[self.IDS] = inttYYY
