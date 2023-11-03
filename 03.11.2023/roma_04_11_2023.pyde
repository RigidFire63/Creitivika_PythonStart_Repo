x=300

def setup():
    size(600,600)
    #background(100,100,100)
    frameRate(10)
    
def draw():
    #background(100,100,100)
    global x
    x=x+5
    ellipse(x,x,70,70)
    ellipse(x,x,70,70)
    ellipse(x,x,70,70)
    ellipse(x,x,70,70) # (=
