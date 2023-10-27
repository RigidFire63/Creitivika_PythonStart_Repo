def setup():
    size(600,600)
    background(0)
    frameRate(1000)
    
def draw():    
    translate(random(-290,290),random(-290,290))
    point(300,random(10,20))
