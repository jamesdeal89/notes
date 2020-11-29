# a 'walker' goes on a random walk and has an equal change of going in any direction. 
# this repeats several times. if done enough times it may hit the 'seed'.
# if it hits the seed, it sticks to it.
# this happens over and over again with a new 'walker'.

from random import choice

def setup():
    global seeds, minDistSq
    size(640//2,480//2)
    seeds = []
    seeds.append((width//2, height//2))
    background(0)
    minDist = 4
    minDistSq = minDist * minDist
    
def draw():
    # loop if particle is not within a mininum distance of a seed
    for i in range(10):
        # make a single particle randomly
        pX, pY = random(0, width), random(0, height)
        stuck = True
        while not stuck:
            # check distance to all seeds
            for seed in seeds:
                dX = seed[0] - pX
                dY = seed[1] - pY
                # do calculation of distance of seed and position
                disSq = abs(dX * dX + dY * dY)
                # check is distance is less than mininum distance
                if disSq < minDistSq:
                    stuck = False
                    seeds.append((pX,pY))
                    break
            # randomly choose a cardinal direction
            bias = 0.01
            walkDir = choice([(0,-1),(1,0),(0,1),(-1,0)])
            pX,pY = pX + walkDir[0], pY + walkDir[1]
            
            if pX < width//2:
                pX += bias
            elif pX > width//2:
                pX -= bias
            if pY < height//2:
                pY += bias
            elif pY > height//2:
                pY -= bias
            
    for seed in seeds:
        strokeWeight(2)
        stroke(255)
        # walk in that direction
        # add the walker to the list of seeds
        # draw the particle on the screen
        point(seed[0],seed[1])
        
    
