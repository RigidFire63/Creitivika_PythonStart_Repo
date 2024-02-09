y=1
mode="больше"
def setup():
    size(600,600)
   
    strokeWeight(5)
    
def draw():
    global y
    
   
    translate(300,300)

    frameRate(60)


    #scale(y)
    background(100)
    rect(30,30,y,y) 
   
    noStroke()
    
    print(y)
    if mode == "больше":
        y=y+1
    if mode == "больше":   
    if mode == "меньше":
         y=y-1
