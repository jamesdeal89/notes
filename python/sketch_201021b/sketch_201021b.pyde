from random import choice

def setup():
    global a,b,c,d,dd
    size(800, 800)
    background(0)
    stroke(255)
    strokeWeight(20)
    a = PVector(0, height)
    b = PVector(width, height)
    c = PVector(width, 0)
    dd = PVector(0,0)
    d = PVector(width/2,height/2)
    
def draw():
    point(d.x,d.y)
    chosen = choice([a,b,c,dd])
    d.x -= (d.x - chosen.x)/2
    d.y -= (d.y - chosen.y)/2
    
    
    
