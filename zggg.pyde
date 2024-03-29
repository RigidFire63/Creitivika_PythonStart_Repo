x=0
mode="вправо"
def setup():
    size(600,600)
    
def draw():
    global x,mode 
    #frameRate(5)
    background(100)
    ellipse(x,20,50,50)
    #x=x+1
    if mousePressed==True:
    
    if mode =="вправо":
        x=x+1
    if mode =="влево": 
        x=x-1  
    if x ==600: 
        mode="влево"   
    if x ==0:
        mode="вправо"
        
