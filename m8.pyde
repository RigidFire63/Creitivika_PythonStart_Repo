x=0
z=0
y=0
def setup():
    global x
    size(1000,1000)
    x=loadImage("m8.png")
    
def draw():
    global x
    image(x,500,100)
    



    global y
    size(1000,1000)
    y=loadImage("m7.png")
    

    global y
    image(y,300,500)
    
    
    
    global z
    size(1000,1000)
    z=loadImage("m1.png")
    
    image(z,50,50,450,450)
