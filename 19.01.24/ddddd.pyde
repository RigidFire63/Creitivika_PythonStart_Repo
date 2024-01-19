y=10
x=0
def setup():
    size(800,800)
    background(97)
    stroke(random(0,255))


def draw():
    global x
    stroke(random(0,255))
    translate(400,400)
    rectMode(CENTER)
    rotate(radians(x))
    ellipse(y, 0, 80, 60)
    x=x+1 
    global y

    y=y+5  
