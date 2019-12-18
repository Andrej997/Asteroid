coordinatesOfRocketsss = []
rocket1xCoordinates = 0
rocket1yCoordinates = 0
rocket1IsDestroyed = 0


def initialize():
    global rocket1xCoordinates
    global rocket1yCoordinates
    rocket1xCoordinates = 1
    rocket1yCoordinates = 1


def isRocketDead():
    global rocket1IsDestroyed
    rocket1IsDestroyed = 1