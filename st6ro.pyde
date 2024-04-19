bg = 0;

def setup():
    size(600,400)
    
def draw():
    
    global bg
   
    if mousePressed==True:
       line (mouseX,mouseY,pmouseX,pmouseY) 
    fill(255)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(250,150,100,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    fill(255,0,0)
    rect(350,140,40,60)
    
    fill(0)
    rect(400,120,90,90)
   
def mouseClicked():
    global bg
    # если прямоугольная кнопка нажата
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
       background(255)
    if mouseX > 350 and mouseX < 430 and mouseY > 140 and mouseY < 200:   
        stroke(255,0,0)
    if mouseX > 400 and mouseX < 520 and mouseY > 90 and mouseY < 180:   
        stroke(0) 
       
