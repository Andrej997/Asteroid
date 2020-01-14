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

HOST = 'localhost'  # The remote host
PORT = 50005        # The same port as used by the server

class NetworkScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        #Server.second_player_is_here = True
        Server.second_player_is_here = False
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
            self.timer = QBasicTimer()
            self.queue = mp.Queue()
            self.queueForPlayer2 = mp.Queue()
            self.timer.start(5, self)

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

            self.omega("pera")
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

            self.omega("player2")
    def omega(self, mssg):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
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
            while not self.queueToSend.empty():
                vals = self.queueToSend.get()
                val_str = vals.__str__()
                self.s.sendall(val_str.encode('utf8'))

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
