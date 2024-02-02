
y=1
def setup():
    size(600,600)
   
    strokeWeight(5)
    
def draw():
    global y
    
   
    translate(300,300)

   
    scale(y)
    background(100)
    ellipse(y,y,250,250) 
   
    noStroke()
    y=y+0.01
    print(y)
    if y  > 1.7:
        y=1
