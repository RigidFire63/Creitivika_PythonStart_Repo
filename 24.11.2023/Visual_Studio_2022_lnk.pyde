s=290
x=700
c=700
y=675
z=725
def setup():
    # тут команды    
    size(600,1000)    
def draw():
    background(130)
    global x
    translate(300,x)
    ellipseMode(CORNER)
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    rotate(radians(30))
    ellipse(0,0,60,20)
    ellipseMode(CENTER)
    ellipse(0,0,20,20)
    line(1,2,1,2)
    x=x-5
