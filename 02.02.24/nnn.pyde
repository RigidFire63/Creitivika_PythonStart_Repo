
y=10
def setup():
    size(600,600)
   
    strokeWeight(5)
    
def draw():
    global y
    
   
    translate(150,150)

   
    background(100)
    ellipse(y,y,250,250) 
    
    noStroke()
    y=y+5
    if y >= 400:
        y=0

    
   
        
