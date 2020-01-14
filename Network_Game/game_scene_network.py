from SpaceShuttle import *
from Asteroid import *
from bonus import *
from game_over_scene import *
from welcome_scene import *
from main import *
from PyQt5.QtCore import pyqtSignal, QBasicTimer, QRectF, QPoint, QTimerEvent, Qt
import multiprocessing as mp
from threading import Thread
import time
import  random
from key_notifier import KeyNotifier
# Echo client program
import socket
from Network_Game.network_asteroids import *
import Server

#HOST = '192.168.0.1'  # The remote host
HOST = 'localhost'
PORT = 50005        # The same port as used by the server

class NetworkScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.connects()
        #self.omega()
        text = ''
        bin = self.s.recv(2048)
        text += str(bin, 'utf-8')
        print(text)
        if text == "1":
            Server.second_player_is_here = False
            #print("labela.")
        elif text == "2":
            Server.second_player_is_here = True

        self.label = QLabel()
        self.pixmap = QPixmap('Images/img2.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)
        self.addWidget(self.label)
        self.asteroid_position_counter = 0
        if Server.second_player_is_here == False:
            self.width = width
            self.height = height
            self.setSceneRect(0, 0, self.width - 2, self.height - 2)
            self.sceneParent = parent

            self.queue = mp.Queue()
            self.queueForPlayer2 = mp.Queue()


            self.label2 = QLabel("Waiting for other clients to connect.")
            self.label2.resize(400, 30)
            self.label2.move(165, 120)
            self.label2.setStyleSheet("font: 12pt; color: #f03a54; font:italic; background-color: transparent; ")
            self.addWidget(self.label2)
            #self.label2.hide()
            self.ply1 = False
            #self.queue.put('go')

            self.checkPlayers = QPushButton("Search opponents")
            self.checkPlayers.setStyleSheet("QPushButton{"
                                         "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                         "}"
                                         "QPushButton:hover{"
                                         "background-color: #C14242"
                                         "}")
            self.checkPlayers.resize(150, 50)
            self.checkPlayers.move(218, 260)
            self.addWidget(self.checkPlayers)

            self.key_notifier = KeyNotifier()
            self.key_notifier.key_signal.connect(self.__update_position__)
            self.key_notifier.start()

            #self.omega("pera")
        elif Server.second_player_is_here == True:
            self.width = width
            self.height = height
            self.setSceneRect(0, 0, self.width - 2, self.height - 2)
            self.sceneParent = parent
            self.queue = mp.Queue()
            self.queueToSend = mp.Queue()

            self.label2 = QLabel("Waiting for other clients to connect.")
            self.label2.resize(400, 30)
            self.label2.move(165, 120)
            self.label2.setStyleSheet("font: 12pt; color: #f03a54; font:italic; background-color: transparent; ")
            self.addWidget(self.label2)
            self.ply1 = False

            self.checkPlayers = QPushButton("Search opponents")
            self.checkPlayers.setStyleSheet("QPushButton{"
                                            "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                            "}"
                                            "QPushButton:hover{"
                                            "background-color: #C14242"
                                            "}")
            self.checkPlayers.resize(150, 50)
            self.checkPlayers.move(218, 260)
            self.addWidget(self.checkPlayers)

            self.key_notifier = KeyNotifier()
            self.key_notifier.key_signal.connect(self.__update_position__)
            self.key_notifier.start()

            #self.omega("player2")

    def connects(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
    def omega(self, mssg):
        #self.s.setblocking(0)
        text2send = '1'
        self.s.sendall(text2send.encode('utf8'))

    def alfa(self):
        if Server.second_player_is_here == False:
            while True:
                text = ''
                bin = self.s.recv(2048)
                text += str(bin, 'utf-8')
                print(text)
                if text == "go":
                    print("labela.")
                    self.createAsteroids()#pocetno kreiranje asteroida
                    self.label2.hide()
                    self.checkPlayers.hide()
                    self.start_new_game()
                    tt = Thread(target=self.recevee)
                    tt.daemon = True
                    tt.start()
                    self.timer = QBasicTimer()
                    self.timer.start(5, self)
                    break
        elif Server.second_player_is_here == True:
            while True:
                text = ''
                bin = self.s.recv(2048)
                text += str(bin, 'utf-8')
                print(text)
                if text == "go":
                    print("labela.")
                    self.createAsteroids()#pocetno kreiranje asteroida
                    self.label2.hide()
                    self.checkPlayers.hide()
                    self.start_new_game()
                    tt = Thread(target=self.recevee)
                    tt.daemon = True
                    tt.start()
                    self.timer = QBasicTimer()
                    self.timer.start(5, self)
                    break

    def start_new_game(self):
        self.set_up_scores_labels()
        if Server.second_player_is_here == False:
            self.rocketnumber1 = SpaceShuttle(self.width, self.height, self, 1)
            self.rocketnumber1.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber1.setStyleSheet("background:transparent")
            self.addWidget(self.rocketnumber1)

            self.rocketnumber2 = SpaceShuttle(self.width, self.height, self, 2)
            self.rocketnumber2.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber2.setStyleSheet("background:transparent")
            self.addWidget(self.rocketnumber2)
        elif Server.second_player_is_here == True:
            self.rocketnumber1 = SpaceShuttle(self.width, self.height, self, 1)
            self.rocketnumber1.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber1.setStyleSheet("background:transparent")
            self.addWidget(self.rocketnumber1)

            self.rocketnumber2 = SpaceShuttle(self.width, self.height, self, 2)
            self.rocketnumber2.resize(60,
                                      50)  # slika je 50x50 ali se glupo okrece tako da je bolje ovako da bi se uvek videla cela
            self.rocketnumber2.setStyleSheet("background:transparent")
            self.addWidget(self.rocketnumber2)


    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        if Server.second_player_is_here == False:
            if key == Qt.Key_Up and Server.player1Lives > 0:
                #self.rocketnumber1.upRocket1.emit()
                self.ply1 = True
                self.queue.put(111)
            if key == Qt.Key_Right and Server.player1Lives > 0:
                #self.rocketnumber1.rightRocket1.emit()
                self.ply1 = True
                self.queue.put(222)
            if key == Qt.Key_Left and Server.player1Lives > 0:
                #self.rocketnumber1.leftRocket1.emit()
                self.ply1 = True
                self.queue.put(333)
            if key == Qt.Key_Space and Server.player1Lives > 0:
                #self.rocketnumber1.fireRocket1.emit()
                self.ply1 = True
                self.queue.put(444)
        elif Server.second_player_is_here == True:
            if key == Qt.Key_W and Server.player2Lives > 0:  # dodata logika da moze da se pomera samo ako je idalje ziva ta raketa
                #self.rocketnumber2.upRocket2.emit()
                self.queueToSend.put(555)
            if key == Qt.Key_A and Server.player2Lives > 0:
                #self.rocketnumber2.leftRocket2.emit()
                self.queueToSend.put(777)
            if key == Qt.Key_D and Server.player2Lives > 0:
                #self.rocketnumber2.rightRocket2.emit()
                self.queueToSend.put(666)
            if key == Qt.Key_S and Server.player2Lives > 0:
                #self.rocketnumber2.fireRocket2.emit()
                self.queueToSend.put(888)

    def timerEvent(self, a0: 'QTimerEvent'):
        if Server.second_player_is_here == False:
            while not self.queue.empty():
                val = self.queue.get()
                val_str = val.__str__()
                self.s.sendall(val_str.encode('utf8'))
            while not self.queueForPlayer2.empty():
                vals = self.queueForPlayer2.get()
                val_str = vals.__str__()
                if val_str == "555":
                    self.rocketnumber2.upRocket2.emit()
                elif val_str == "666":
                    self.rocketnumber2.rightRocket2.emit()
                elif val_str == "777":
                    self.rocketnumber2.leftRocket2.emit()
                elif val_str == "888":
                    self.rocketnumber2.fireRocket2.emit()
                elif val_str == "111":
                    self.rocketnumber1.upRocket1.emit()
                elif val_str == "222":
                    self.rocketnumber1.rightRocket1.emit()
                elif val_str == "333":
                    self.rocketnumber1.leftRocket1.emit()
                elif val_str == "444":
                    self.rocketnumber1.fireRocket1.emit()
        elif Server.second_player_is_here == True:
            while not self.queueToSend.empty():
                vals = self.queueToSend.get()
                val_str = vals.__str__()
                self.s.sendall(val_str.encode('utf8'))
            while not self.queue.empty():
                val = self.queue.get()
                # print("dobio")
                # print(val)
                val_str = val.__str__()
                if val_str == "111":
                    self.rocketnumber1.upRocket1.emit()
                elif val_str == "222":
                    self.rocketnumber1.rightRocket1.emit()
                elif val_str == "333":
                    self.rocketnumber1.leftRocket1.emit()
                elif val_str == "444":
                    self.rocketnumber1.fireRocket1.emit()
                elif val_str == "555":
                    self.rocketnumber2.upRocket2.emit()
                elif val_str == "666":
                    self.rocketnumber2.rightRocket2.emit()
                elif val_str == "777":
                    self.rocketnumber2.leftRocket2.emit()
                elif val_str == "888":
                    self.rocketnumber2.fireRocket2.emit()

    def recevee(self):
        if Server.second_player_is_here == False:
            while True:
                text = ''
                print("cekam recv neki")
                bin = self.s.recv(2048)
                text += str(bin, 'utf-8')
                print("dobio recv")
                print(text)
                self.queueForPlayer2.put(text)
        elif Server.second_player_is_here == True:
            while True:
                text = ''
                print("cekam recv neki")
                bin = self.s.recv(2048)
                text += str(bin, 'utf-8')
                print("dobio recv")
                print(text)
                self.queue.put(text)


    def createAsteroids(self):
        o = 0
        for o in range(Server.level):
            self.asteroid_position_counter += 1
            self.asteroid_0 = NetworkAsteroid(self.width, self.height, self, Server.asteroid_id.__str__(), False, 3, self.asteroid_position_counter)
            self.asteroid_0.setFocus()  # mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            #activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[Server.asteroid_id.__str__()] = 0
            Server.asteroid_id = Server.asteroid_id.__int__() + 1

    def createMediumAsteroids(self):
        o = 0
        for o in range(2):
            self.asteroid_position_counter += 1
            self.asteroid_0 = NetworkAsteroid(self.width, self.height, self, Server.asteroid_id.__str__(), False, 2, self.asteroid_position_counter)
            self.asteroid_0.setFocus()  # mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            #activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[Server.asteroid_id.__str__()] = 0
            Server.asteroid_id = Server.asteroid_id.__int__() + 1

    def createSmallAsteroids(self):
        o = 0
        for o in range(2):
            self.asteroid_position_counter += 1
            self.asteroid_0 = NetworkAsteroid(self.width, self.height, self, Server.asteroid_id.__str__(), False, 1, self.asteroid_position_counter)
            self.asteroid_0.setFocus()  # mozda i ne mora posto je timer tamo
            self.asteroid_0.setStyleSheet("background:transparent")
            self.asteroid_0.resize(60, 50)
            self.addWidget(self.asteroid_0)
            #activeBigAsteroids.append(self.asteroid_0)
            Server.activeAsteroids[Server.asteroid_id.__str__()] = 0
            Server.asteroid_id = Server.asteroid_id.__int__() + 1

    def set_up_scores_labels(self):
        self.label11 = QLabel(
            "Player1 lives--->[" + Server.player1Lives.__str__() + "] score--->[" + Server.player1Score.__str__() + "]")
        self.label11.resize(400, 30)
        self.label11.move(5, 440)
        self.label11.setStyleSheet("font: 9pt; color: #f03a54; font:bold; background-color: transparent; ")
        self.addWidget(self.label11)

        self.label22 = QLabel(
            "Player2 lives--->[" + Server.player2Lives.__str__() + "] score--->[" + Server.player2Score.__str__() + "]")
        self.label22.resize(400, 30)
        self.label22.move(5, 470)
        self.label22.setStyleSheet("font: 9pt; color: yellow; font:bold; background-color: transparent; ")
        self.addWidget(self.label22)

        self.label33 = QLabel(
            "Player3 lives--->[" + Server.player3Lives.__str__() + "] score--->[" + Server.player3Score.__str__() + "]")
        self.label33.resize(400, 30)
        self.label33.move(320, 440)
        self.label33.setStyleSheet("font: 9pt; color: blue; font:bold; background-color: transparent; ")
        self.addWidget(self.label33)

        self.label44 = QLabel(
            "Player4 lives--->[" + Server.player4Lives.__str__() + "] score--->[" + Server.player4Score.__str__() + "]")
        self.label44.resize(400, 30)
        self.label44.move(320, 470)
        self.label44.setStyleSheet("font: 9pt; color: green; font:bold; background-color: transparent; ")
        self.addWidget(self.label44)

        self.labelLevel = QLabel("Level : " + Server.level.__str__())
        self.labelLevel.resize(400, 30)
        self.labelLevel.move(500, 10)
        self.labelLevel.setStyleSheet("font: 9pt; color: white; font: bold; background-color: transparent;")
        self.addWidget(self.labelLevel)

    def game_is_over(self, playerId):  # ako je game over proveri za kog igraca je game over ako je multiplayer, onog drugog pusti da jos igra
        if playerId == 1:
            Server.coordinatesOfRocket1X.clear()
            Server.coordinatesOfRocket1Y.clear()
            self.rocketnumber1.hide()
            self.rocketnumber1.move(1000, 1000)
        elif playerId == 2:
            Server.coordinatesOfRocket2X.clear()
            Server.coordinatesOfRocket2Y.clear()
            self.rocketnumber2.hide()
            self.rocketnumber2.move(1000, 1000)

        if Server.player1Lives == 0 and Server.player2Lives == 0:  # ako su dva playera, tek kada su oba mrtva prebaci na game_over_scene
            self.gameOverScene = GameOver(self, self.width, self.height)
            self.gameOverScene.returnBtn.clicked.connect(self.menus)
            self.gameOverScene.label6.hide()
            #self.gameOverScene.label2.hide()
            self.gameOverScene.label3.hide()
            self.gameOverScene.label4.hide()
            self.gameOverScene.label5.hide()
            if Server.player1Score > Server.player2Score:
                self.gameOverScene.label2.setText("Network game winner is Player1.")
            else:
                self.gameOverScene.label2.setText("Network game winner is Player2.")
                self.gameOverScene.label2.setStyleSheet("font: 9pt; color: yellow; font:bold; background-color: transparent; ")
            self.gameOverScene.label2.move(140, 350)
            self.sceneParent.setScene(self.gameOverScene)

    def menus(self):
        self.sceneParent.ExitGame()
