x=100

def setup():
    size(400,600)
    #background(100,100,100)
    frameRate(10)
    
def draw():
    background(100,100,100)
    global x
    x=x+5
    ellipse(x,x,random(10,70),random(10,70))
