def setup():
    global snow, wind
    size(800,600)
    snow = []
    wind = random(-2,2)
    for i in range(100):
        snow.append([random(0,width), random(-height,0), random(0.5,2)])
    

def draw():
    background(0)
    for flake in snow:
        flake[1] += 1 * flake[2]
        flake[0] += wind
        if flake[1] > height:
            flake[1] = 0
            flake[0] = random(0,width) 
    stroke(255)
    for flake in snow:
        strokeWeight(3 * flake[2])
        point(flake[0],flake[1])
    
