from PyQt5.QtCore import QSize, QDir, Qt
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel
import Server


class GameOver(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.width = width
        self.height = height

        self.label = QLabel()
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(600, 500)
        self.addWidget(self.label)

        self.mainLabel = QLabel("GAME OVER!")
        self.mainLabel.resize(200, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.mainLabel.move(200, 0)
        self.addWidget(self.mainLabel)

        self.returnBtn = QPushButton("EXIT")
        self.returnBtn.setStyleSheet("QPushButton{"
                                     "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                     "}"
                                     "QPushButton:hover{"
                                     "background-color: #C14242"
                                     "}")
        self.returnBtn.resize(100, 50)
        self.returnBtn.move(250, 230)
        self.addWidget(self.returnBtn)

        self.label2 = QLabel(
            "Player1 lives--->[" + server.player1Lives.__str__() + "] score--->[" + server.player1Score.__str__() + "]")
        self.label2.resize(400, 30)
        self.label2.move(5, 440)
        self.label2.setStyleSheet("font: 12pt; color: #f03a54; font:bold; background-color: transparent; ")
        self.addWidget(self.label2)

        self.label3 = QLabel(
            "Player2 lives--->[" + server.player2Lives.__str__() + "] score--->[" + server.player2Score.__str__() + "]")
        self.label3.resize(400, 30)
        self.label3.move(5, 470)
        self.label3.setStyleSheet("font: 12pt; color: yellow; font:bold; background-color: transparent; ")
        self.addWidget(self.label3)