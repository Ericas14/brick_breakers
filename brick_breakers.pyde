ball_x = random(0,600)
x_speed = 4
ball_y = random(200,400)
y_speed = 4
showing1 = True
showing2 = True
showing3 = True
showing4 = True
showing5 = True
showing6 = True
showing7 = True
showing8 = True
showing9 = True
showing10 = True
showing11 = True
showing12 = True
points = 0
def setup():
    size(600,600)
    background(0,0,0)
    fill(255,255,255)
    fill(random(0,255),random(0,255),random(0,255))
   
    
def draw():
    global ball_x
    global ball_y
    global y_speed
    global x_speed
    global showing1
    global showing2
    global showing3
    global showing4
    global showing5
    global showing6
    global showing7
    global showing8
    global showing9
    global showing10
    global showing11
    global showing12
    global points
    background(0,0,0)
   # fill(252, 207, 248)
    ellipse(ball_x,ball_y,30,30)
    rect(mouseX-50,500, 100,20)
    textSize(32)
    text("Points: ", 0,600)
    text(points,115,600) 
    
    if ball_y < 15:
        y_speed = -y_speed
    if (485 < ball_y < 500) and (mouseX-100 < ball_x < mouseX+50): 
        y_speed = -y_speed
    if ball_x < 15: 
        x_speed = -x_speed
    if ball_x > 585:
         x_speed = -x_speed
         
    if showing1:
        rect(0,0,100,70) 
    
        if (0 < ball_x < 100) and ball_y < 85:
                y_speed = -y_speed
                showing1 = False
                points = points + 10
               
    if showing2:
        rect(100,0,100,70) 
    
        if (100 < ball_x < 200) and ball_y < 85:
                y_speed = -y_speed
                showing2 = False
                points = points + 10
             
    
    if showing3:
        rect(200,0,100,70) 
    
        if (200 < ball_x < 300) and ball_y < 85:
                y_speed = -y_speed
                showing3 = False
                points = points + 10
             
               
    if showing4:
        rect(300,0,100,70) 
            
        if (300 < ball_x < 400) and ball_y < 85:
                y_speed = -y_speed
                showing4 = False
                points = points + 10
            
               
    if showing5:
        rect(400,0,100,70) 
    
        if (400 < ball_x < 500) and ball_y < 85:
                y_speed = -y_speed
                showing5 = False
                points = points + 10
               
    if showing6:
        rect(500,0,100,70) 
            
        if (500 < ball_x < 600) and ball_y < 85:
                y_speed = -y_speed
                showing6 = False
                points = points + 10 
    if showing7:
        rect(0,70,100,70) 
    
        if (0 < ball_x < 100) and ball_y < 170:
                y_speed = -y_speed
                showing7 = False
                points = points + 10
               
    if showing8:
        rect(100,70,100,70) 
    
        if (100 < ball_x < 200) and ball_y < 170:
                y_speed = -y_speed
                showing8 = False
                points = points + 10
             
    
    if showing9:
        rect(200,70,100,70) 
    
        if (200 < ball_x < 300) and ball_y < 170:
                y_speed = -y_speed
                showing9 = False
                points = points + 10
             
               
    if showing10:
        rect(300,70,100,70) 
            
        if (300 < ball_x < 400) and ball_y < 170:
                y_speed = -y_speed
                showing10 = False
                points = points + 10
            
               
    if showing11:
        rect(400,70,100,70) 
    
        if (400 < ball_x < 500) and ball_y < 170:
                y_speed = -y_speed
                showing11 = False
                points = points + 10
               
    if showing12:
        rect(500,70,100,70) 
            
        if (500 < ball_x < 600) and ball_y < 170:
                y_speed = -y_speed
                showing12 = False
                points = points + 10
    if points == 120:
       textSize(60)
       text("You Win!", 148,300)
    elif ball_y > 600:
        textSize(60)
        text("You Lose!", 148,300)             
   
             
     #rect(100,1,100,70)
    
    # rect(200,0, 100, 70)
    
    # rect (300,0,100,70)
    
    # rect(400,0,100,70)
    
    # print("showing", showing)
    
    # rect(500,0,100,70) 
    
    
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed
     
