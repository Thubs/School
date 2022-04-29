import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

Ed.ObstacleDetectionBeam(Ed.ON)

SideTurn = 0
obstacle = 0
obstacle = Ed.ReadObstacleDetection()
Ed.Drive(Ed.FORWARD, Ed.SPEED_10, 25)

while yes == no():
    Ed.Drive(Ed.FORWARD, Ed.SPEED_10, 25)
    yes = yes + 1

while True:
	Ed.Drive(Ed.FORWARD, Ed.SPEED_10, Ed.DISTANCE_UNLIMITED)
	if obstacle>Ed.OBSTACLE_NONE:
		Ed.Drive(Ed.BACKWARD, Ed.SPEED_10, 3)
		if obstacle==Ed.OBSTACLE_LEFT:
			Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_10, 90)
		elif obstacle==Ed.OBSTACLE_RIGHT:
			Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_10, 90)
		elif obstacle==Ed.OBSTACLE_AHEAD:
			if SideTurn ==1:
				Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_10, 90)
			else:
				Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_10, 90)
				
		SideTurn=0
	else:
		SideTurn=1
