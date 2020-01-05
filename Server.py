coordinatesOfRocketsX = []
coordinatesOfRocketsY = []

activeAsteroids = {}

player1Lives = 3
player1Hitted = 0
player2Lives = 3
player2Hitted = 0

player1Score = 0
player2Score = 0
player3Score = 0
player4Score = 0

#metkoviCoordsX = []
#metkoviCoordsY = []

bulletsCollectionX = {}
bulletsCollectionY = {}
bulletIDS = 0
bulletsCounter = 0
rocket1_bulletsCounter = 0
rocket2_bulletsCounter = 0
maximum_of_bullets = 31

level = 1   #globalna promenljiva koja odredjuje trenutni nivo
            #i na osnovu nje se kreiraju asteroidi

bonus_time = 0 #bonus dolazi na svakih 10 sekundi [5*2]
bonus_x_coordinate = 0
bonus_x_expanded = []
bonus_y_coordinate = 0
bonus_y_expanded = []