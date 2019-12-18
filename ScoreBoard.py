from PyQt5.QtWidgets import QLabel
from SpaceShuttle import Mover

class ScoreBoard(QLabel):
    def __init__(self, x, y, spaceShut: Mover):
        self.move(x,y)
        self.setStyleSheet("background-color:transparent")
        self.textFormat("lives: {0}, score: {1}", spaceShut.myLives, spaceShut.score)