coordinatesOfRocket1X = []
coordinatesOfRocket1Y = []
coordinatesOfRocket2X = []
coordinatesOfRocket2Y = []

activeAsteroids = {}
bar_jedan_je_ziv_asteroid = False
asteroid_id = 0
num_of_active_asteroids = 1

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

bulletsCollection1X = {}
bulletsCollection1Y = {}
bulletsCollection2X = {}
bulletsCollection2Y = {}
bulletIDS = 0
bulletsCounter = 0
rocket1_bulletsCounter = 0
rocket2_bulletsCounter = 0
maximum_of_bullets = 16

level = 1   #globalna promenljiva koja odredjuje trenutni nivo
            #i na osnovu nje se kreiraju asteroidi

bonus_time = 0 #bonus dolazi na svakih 10 sekundi [5*2]
bonus_x_coordinate = 0
bonus_x_expanded = []
bonus_y_coordinate = 0
bonus_y_expanded = []