x=400
y=400
def setup():
    size(800, 800)  
    strokeWeight(10)
def draw():
    # тут команды
    global x, y
    stroke(234,0,0)
    line(400,400,x,y)
    x=x+5
