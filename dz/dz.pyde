y=5
def setup():
    size(800,800)
    background(0)
def draw():
    global y
    stroke(random(0,255),random(0,255),random(0,255))
    point(random(1,800),random(1,800))
    strokeWeight(random(0,5))
    y=y+1
    if frameCount%1000 == 0:
        background(0)
