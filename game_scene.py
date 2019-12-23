from SpaceShuttle import *
from asteroid import *
from game_over_scene import *
from welcome_scene import *
from main import *

activeBigAsteroids = []
activeMediumAsteroids = []
activeSmallAsteroids = []


class GameScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        global activeBigAsteroids
        global activeMediumAsteroids
        global activeSmallAsteroids
        self.width = width
        self.height = height
        self.setSceneRect(0, 0, self.width-2, self.height-2)
        self.sceneParent = parent#

        self.label = QLabel()
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)
        self.addWidget(self.label)

        self.rocketnumber1 = SpaceShuttle(self.width, self.height, self, 1)
        self.rocketnumber1.resize(60, 50)#slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
        self.rocketnumber1.setStyleSheet("background:transparent")
        self.addWidget(self.rocketnumber1)
        self.rocketnumber1.setFocus()

        o = 0
        for o in range(5):
            self.asteroid_0 = Asteroid(self.width, self.height, self, o.__str__())
            self.asteroid_0.setFocus()#mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[o.__str__()] = 0

        print("DONE")

        self.label2 = QLabel(
            "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
        self.label2.resize(400, 30)
        self.label2.move(5, 440)
        self.label2.setStyleSheet("font: 12pt; color: #f03a54; font:bold; background-color: transparent; ")
        self.addWidget(self.label2)

        self.label3 = QLabel(
            "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
        self.label3.resize(400, 30)
        self.label3.move(5, 470)
        self.label3.setStyleSheet("font: 12pt; color: yellow; font:bold; background-color: transparent; ")
        self.addWidget(self.label3)

    def game_is_over(self):#ako je game over
        self.gameOverScene = GameOver(self, self.width, self.height)
        self.gameOverScene.returnBtn.clicked.connect(self.menus)
        self.sceneParent.setScene(self.gameOverScene)

    def menus(self):
        self.sceneParent.ExitGame()
