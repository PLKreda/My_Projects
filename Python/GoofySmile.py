# THIS IS SO GOOFY ISTG LFMAO
import turtle as t

t.bgcolor("black")
t.color("WHITE")
t.speed(10000000)

def createEye():
    t.setheading(0)
    for i in range(32*4):
        t.back(120)
        t.right(120+1)

def CreateSmile():
    t.penup()
    t.goto(0,-50)
    t.back(200)
    t.pendown()
    t.forward(60)
    t.right(25)
    t.forward(120)
    t.right(-25)
    t.forward(120)
    t.right(-25)
    t.forward(120)
    t.right(25)
    t.forward(60)

def createEyes():
    t.penup()
    t.back(50)
    t.pendown()
    createEye()
    t.penup()
    t.goto(200,0)
    t.pendown()
    t.right(0)
    createEye()
    t.setheading(0)



createEyes()
CreateSmile()

t.done()
