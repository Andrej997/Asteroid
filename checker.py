from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
from game_scene import *

class Checker(QObject):

    check_signal = pyqtSignal("""int""")

    def __init__(self):
        super().__init__()

    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while True :
            time.sleep(0.5)
            print("Alo")
            if Server.activeAsteroids.__len__() > 0:
                counterActAst = 0
                for ast in Server.activeAsteroids:
                    if (Server.activeAsteroids[ast] == 1):
                        counterActAst = counterActAst + 1
                if counterActAst == Server.activeAsteroids.__len__():
                    Server.level = Server.level + 1
                    Server.create = True
                else :
                    Server.create = False
