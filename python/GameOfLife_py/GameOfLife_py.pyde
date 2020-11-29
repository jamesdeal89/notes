# Conway's Game Of Life
def setup():
    size(80, 60)

def draw():
    background(0)
    # generate a series of random points to be 'alive'
    theLiving = []
    for x in range(1,20):
        # white colour for alive cells
        stroke(255)
        randomAlive = []
        # first find random x co-ordinate
        randomAlive.append(random(0, 80))
        # then find random y co-ordinate
        randomAlive.append(random(0,60))
        # now draw the random point
        point(randomAlive[0], randomAlive[1]) 
        theLiving.append(randomAlive[0])
        theLiving.append(randomAlive[1])
        # for loop repeats until 20 living cells are created
    yCheck = 1
    for checkLife in range(0,80):
        
        yCheck += 1
        if yCheck == 61:
            break
        # check the number of also alive points surrounding it in all directions
    
    # if the number of 'alive' surrounding points is less than 2, it 'dies'
    # if the number of 'alive' surrounding points is greater than 3, it 'dies'
    # if the number of 'alive' surrounding points is equal to 2 or 3, it 'lives'
    # if there is a point with three living neighbors, it becomes 'alive'
