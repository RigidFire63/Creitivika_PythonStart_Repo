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
    line(0, 0, 20, 200)
    x=x+1 
      
