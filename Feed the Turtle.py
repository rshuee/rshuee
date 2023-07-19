#FEED THE TURTLE

import turtle
import random       #Food Positions at Random

#Turtle sprite
t=turtle.Turtle()
t.color('green','lime')
t.shape('turtle')
t.shapesize(3,3,3)

#Food sprite
f=turtle.Turtle()
f.shape('circle')
f.color('red','yellow')

#Remove Trail
t.penup()
f.penup()

#Key Functions
def up():
    t.setheading(90)
    t.fd(10)
    move()
    
def down():
    t.setheading(270)
    t.fd(10)
    move()
    
def left():
    t.setheading(180)
    t.fd(10)
    move()

def right():
    t.setheading(0)
    t.fd(10)
    move()

#Food Positions at Random
c=turtle.Screen()

def pos():
    f.goto(random.randrange(-200,200,10),random.randrange(-200,200,10))
    c.ontimer(pos,10000)

pos()

#Computer Inputs
turtle.listen()
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')
turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')

#Auto Target and Score
def move():
    global s
    if round(t.xcor())==round(f.xcor())and round(t.ycor())==round(f.ycor()):
        f.goto(random.randrange(-200,200,10),random.randrange(-200,200,10))
        s=s+1
        print('Food Eaten',s)
        if s==10:
            print('Your Turtle is Full!')
            t.hideturtle()
            f.hideturtle()

#Score
s=0



