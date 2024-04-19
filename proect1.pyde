bg = 0;

def setup():
    size(1000,1000)
    background(255)
def draw():
   
    global bg
   
    if mousePressed==True:
       line (mouseX,mouseY,pmouseX,pmouseY) 
    fill(255)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(250,30,100,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    fill(255,0,0)
    rect(350,30,40,60)
    fill(0)
    rect(400,30,90,90)#black
    fill(12,7,216)
    rect(490,30,120,100)





def mouseClicked():
    global bg

    # если прямоугольная кнопка нажата
    if mouseX > 250 and mouseX < 350 and mouseY > 30 and mouseY < 90:
        background(255)
    if mouseX > 350 and mouseX < 390 and mouseY > 40 and mouseY < 100:   
        stroke(255,0,0)
    if mouseX > 400 and mouseX < 490 and mouseY > 30 and mouseY < 120:   
        stroke(0) 
    if mouseX > 490 and mouseX < 610 and mouseY > 30 and mouseY < 130:  
        stroke(0,0,255)
    


    
