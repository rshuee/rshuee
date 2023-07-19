#SNAKE GAME

import turtle
import random   #Place food 

#Imortant Variables
a=0  #Score Variable   
b=0  #Size of the Snake    
fx=0 #Food variable for placing food on x=axis
fy=0 #Food variable fro placing food on y=axis
ft=0 

#Home Screen (Display play)
def home():
    turtle.clear()
    turtle.goto(0,0)        #Location
    turtle.hideturtle()     #Hide the turtle
    turtle.write('Play the Snake Game',font=('calibri',20)) #Home message
    turtle.onscreenclick(start)  #When clicked play

#Clear Screen once play
def start(x,y):
    global a,b,fx,fy,ft

    
    turtle.onscreenclick(None)  #Removes the start call
    turtle.clear()
    turtle.speed(0)             #Drawing graphics takes less time (from 0-10)
    turtle.pu()                 #Remove line (penup)
    turtle.goto(-220,220)       #Move turtle to make bounderies
    turtle.color('red')         #Changes the color of bounderies
    turtle.pensize(20)          #Thickness of the bounderies
    turtle.pd()                 #Add bounderies/trail (pendown)
    turtle.goto(220,220)        #Square trail
    turtle.goto(220,-220)       #Square trail
    turtle.goto(-220,-220)      #Square trail
    turtle.goto(-220,220)       #Square trail
    turtle.pu()                 #Remove Trail
    turtle.goto(0,0)            #Spawn at center

#Food Sprite
    tfood=turtle.Turtle()
    tfood.shape('circle')
    tfood.color('yellow')
    tfood.pu()

#Import New Turtle for the Score
    tscore=turtle.Turtle()              #Insert new turtle call tscore
    tscore.penup()                      #Remove trail
    tscore.goto(60,-260)                #Move turtle to area we want the score
    tscore.hideturtle()                 #Hide the arrow
    tscore.write('Score = '+ str(a),font=('calibri',20,'italic'))#Message, add a variable as a string

    while x>-200 and x<200 and y>-200 and y<200:
        if ft==0:
            food(tfood)#Call the function and passing the variable by defining it
            ft=1
        x=turtle.xcor()
        y=turtle.ycor()
        move()  #Call the move function
        turtle.listen() #Focus on the keyboard
        turtle.onkey(up,'Up')
        turtle.onkey(down,'Down')
        turtle.onkey(left,'Left')
        turtle.onkey(right,'Right')
        
        if x>fx-15 and x<fx+15 and y>fy-15 and y<fy+15:
            a+=1   #another way of writing a=a+1
            tscore.clear()
            tfood.clear()
            tscore.write('Score= '+ str(a),font=('calibri',20,'italic'))
            ft=0
    tscore.clear()
    tfood.clear()
    turtle.clear()
    gameover()
    
def move():
    global a,b    #Even a,b are global, if you change the value of a,b then it will not be able to define a,b
    turtle.shape('square')
    turtle.color('blue')
    turtle.stamp()      #Creating duplicates of turtles
    turtle.forward(10)
    if b>a:             
        turtle.clearstamps(1)
    else:
        b=b+1

def food(tfood):
    global fx,fy    #Even fx,fy are global, if you change the value of fx,fy then it will not be able to define fx,fy
    fx=random.randrange(-160,160,10)    #-160,-150,-140,...,0,10,20,...,150,160
    fy=random.randrange(-160,160,10)
    tfood.hideturtle()
    tfood.goto(fx,fy)   #Fx,fy means that tfood goes on random position
    tfood.stamp()

#Key Function
def up():
    turtle.setheading(90)

def down():
    turtle.setheading(270)

def right():
    turtle.setheading(0)

def left():
    turtle.setheading(180)

def gameover():
    turtle.goto(-110,50)
    turtle.color('black')
    turtle.write('Game Over',font=('calibri',40,'bold'))
    turtle.goto(-90,-50)
    turtle.color('red')
    turtle.write('Score= '+ str(a),font=('calibri',40,'bold'))

home()  #Call home function
