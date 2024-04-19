# bg = 0;

# def setup():
#     size(600,400)
    
# def draw():
#     global bg
#     background(bg)
#     fill(255)

#     ellipse(400,350,70,70) # центр х=400 y=350 диаметр 70, радиус 35
        
# def mouseClicked():
#     global bg
#      #если круглая кнопка нажата
#     xDif = 400 - mouseX
#     yDif = 350 - mouseY
    
#     if sqrt(xDif*xDif + yDif*yDif) < 35:
#         bg = 0

x=0
y=0
z=0
bg=250
sw=5
def setup():
    global x
    global y
    global z
    global bg
    global sw
    
    textSize(12)
    size(800,800)
    background(250)
    strokeWeight(sw)
    frameRate(100)
    
def draw():
    global bg
    global sw
    global x
    global z
    global y
        
