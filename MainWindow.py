from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap, QMoveEvent

import sys
from SpaceShuttle import *
import multiprocessing as mp
import time

def changeWindow(w1, w2):
        w2.show()
        w1.hide()

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        #self.newGameWindow = NewGameWindow()
        #self.setStyleSheet("background-image: url(C:\\Users\\Mistra\\Desktop\\Pajton\\vjezba\\asteroid.jpg)")
        #self.setStyleSheet("background-color:black")
        self.setWindowTitle("Asteroids")
        #self.setGeometry(300, 150, 600, 500)
        self.setFixedSize(600, 500)
        
        # background image
        self.label = QLabel(self)
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)

        self.mainLabel = QLabel("ASTEROIDS", self)
        self.mainLabel.resize(200,100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold")
        self.mainLabel.move(200, 0)
        
        self.newGameBtn = QPushButton("New Game",  self)
        self.newGameBtn.setStyleSheet("color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white")
        self.newGameBtn.resize(100, 50)
        self.newGameBtn.move(250, 100)
        self.newGameBtn.clicked.connect(self.startNewGameWindow)

        self.aboutGameBtn = QPushButton("About game", self)
        self.aboutGameBtn.setStyleSheet("color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white")
        self.aboutGameBtn.resize(100, 50)
        self.aboutGameBtn.move(250, 165)

        self.exitBtn = QPushButton("Exit game", self)
        self.exitBtn.setStyleSheet("color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white")
        self.exitBtn.resize(100, 50)
        self.exitBtn.move(250, 230)
        self.exitBtn.clicked.connect(self.close)

        self.mainLabelNewGame = QLabel("Chose game mode", self)
        self.mainLabelNewGame.resize(300, 100)
        self.mainLabelNewGame.setStyleSheet("color: white; font-size:32px; font:bold")
        self.mainLabelNewGame.move(150, 0)
        self.mainLabelNewGame.hide()

        self.singlPlyBtn = QPushButton("Single player", self)
        self.singlPlyBtn.setStyleSheet("color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white")
        self.singlPlyBtn.resize(100, 50)
        self.singlPlyBtn.move(250, 100)
        self.singlPlyBtn.clicked.connect(self.startGame)
        self.singlPlyBtn.hide()

        self.multiPlyBtn = QPushButton("Multiplayer", self)
        self.multiPlyBtn.setStyleSheet("color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white")
        self.multiPlyBtn.resize(100, 50)
        self.multiPlyBtn.move(250, 165)
        self.multiPlyBtn.hide()
        
        self.returnBtn = QPushButton("Return", self)
        self.returnBtn.setStyleSheet("color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white")
        self.returnBtn.resize(100, 50)
        self.returnBtn.move(250, 230)
        self.returnBtn.hide()
        self.returnBtn.clicked.connect(self.returnToMainWindow)
     
        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        #label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        #self.setCentralWidget(label)

    def startNewGameWindow(self):
        self.mainLabel.hide()
        self.newGameBtn.hide()
        self.aboutGameBtn.hide()
        self.exitBtn.hide()
        self.mainLabelNewGame.show()
        self.singlPlyBtn.show()
        self.multiPlyBtn.show()
        self.returnBtn.show()
        #bit = window.pos().x() + 1
        #bit2 = window.pos().y() + 30 +1
        #window1.setGeometry(bit, bit2, 600, 500)
        #changeWindow(window, window1)
    
    def returnToMainWindow(self):
        self.mainLabel.show()
        self.newGameBtn.show()
        self.aboutGameBtn.show()
        self.exitBtn.show()
        self.mainLabelNewGame.hide()
        self.singlPlyBtn.hide()
        self.multiPlyBtn.hide()
        self.returnBtn.hide()

    def close(self):
        app.closeAllWindows()
    
    def startGame(self):
        bit = window.pos().x() + 1
        bit2 = window.pos().y() + 30 + 1
        gameStart.setGeometry(bit, bit2, 600, 500)
        changeWindow(window, gameStart)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #window1 = NewGameWindow()
    gameStart = SpaceShuttle()
    #gameStart.hide()
    app.exec_()