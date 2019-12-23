from SpaceShuttle import *
from asteroid import *
from game_over_scene import *
from welcome_scene import *
from main import *
import multiprocessing as mp
from threading import Thread

activeBigAsteroids = []
activeMediumAsteroids = []
activeSmallAsteroids = []


class GameScene(QGraphicsScene):
    def __init__(self, parent, width, height, num_of_players):
        super().__init__(parent)
        global activeBigAsteroids
        global activeMediumAsteroids
        global activeSmallAsteroids
        self.width = width
        self.height = height
        self.setSceneRect(0, 0, self.width-2, self.height-2)
        self.sceneParent = parent#
        self.players_number = num_of_players
        self.queue = mp.Queue()
        self.firstrelease = False
        self.keyList = []


        self.label = QLabel()
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)
        self.addWidget(self.label)

        self.rocketnumber1 = SpaceShuttle(self.width, self.height, self, 1)
        self.rocketnumber1.resize(60, 50)#slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
        self.rocketnumber1.setStyleSheet("background:transparent")
        self.addWidget(self.rocketnumber1)

        if self.players_number == 2:
            self.rocketnumber2 = SpaceShuttle(self.width, self.height, self, 2)
            self.rocketnumber2.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber2.setStyleSheet("background:transparent")
            self.addWidget(self.rocketnumber2)


        self.queue.put('go')
        tt = Thread(target=self.infiniteFunction)
        tt.start()

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


    def infiniteFunction(self):
        while True:
            num = self.queue.get()
            print("Got {0}".format(num))
            if num == 1:
                self.rocketnumber1.leftRocket1.emit()
            elif num == 2:
                self.rocketnumber1.upRocket1.emit()
            elif num == 3:
                self.rocketnumber1.rightRocket1.emit()
            elif num == 4:
                self.rocketnumber1.fireRocket1.emit()
            elif num == 5 and self.players_number == 2:
                self.rocketnumber2.leftRocket2.emit()
            elif num == 6 and self.players_number == 2:
                self.rocketnumber2.upRocket2.emit()
            elif num == 7 and self.players_number == 2:
                self.rocketnumber2.rightRocket2.emit()
            elif num == 8 and self.players_number == 2:
                self.rocketnumber2.fireRocket2.emit()

    def keyPressEvent(self, event):
        self.firstrelease = True
        my_key = event.key()
        self.keyList.append(my_key)

    def keyReleaseEvent(self, event):
        if self.firstrelease == True:
            self.processmultikeys(self.keyList)

        self.firstrelease = False
        del self.keyList[-1]

    def processmultikeys(self, keyspressed):
        if 16777234 in keyspressed:#1L
            self.queue.put(1)
        if 16777235 in keyspressed:#1Up
            self.queue.put(2)
        if 16777236 in keyspressed:#1R
            self.queue.put(3)
        if 32 in keyspressed:#1Fire
            self.queue.put(4)
        if self.players_number == 2:
            if 65 in keyspressed:#2L
                self.queue.put(5)
            if 87 in keyspressed:#2Up
                self.queue.put(6)
            if 68 in keyspressed:#2R
                self.queue.put(7)
            if 83 in keyspressed:#2Fire
                self.queue.put(8)
        print(keyspressed)