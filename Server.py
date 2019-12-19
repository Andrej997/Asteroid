coordinatesOfRocketsX = []
coordinatesOfRocketsY = []
rocket1xCoordinates = 0
rocket1yCoordinates = 0
rocket1IsDestroyed = 0
player1Lives = 3
player1Score = 0
player2Score = 0
player3Score = 0
player4Score = 0

def initialize():
    global rocket1xCoordinates
    global rocket1yCoordinates
    global coordinatesOfRocketsX
    global coordinatesOfRocketsY
    rocket1xCoordinates = 1
    rocket1yCoordinates = 1


def isRocketDead():
    global rocket1IsDestroyed
    rocket1IsDestroyed = 1