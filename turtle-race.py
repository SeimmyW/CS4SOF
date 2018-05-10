#Turtle Race

from turtle import *
from random import randint


speed(10)
penup()
goto(-140,140)
for step in range(12):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

    
ada=Turtle() #ada, blue, yellow, and green are 4 different objects
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

blue=Turtle()
blue.color('blue')
blue.shape('turtle')

blue.penup()
blue.goto(-160,66)
blue.pendown()

green=Turtle()
green.color('green')
green.shape('turtle')

green.penup()
green.goto(-160,33)
green.pendown()

yellow=Turtle()
yellow.color('gold')
yellow.shape('turtle')

yellow.penup()
yellow.goto(-160,0)
yellow.pendown()

for turn in range (100):
    ada.forward(randint(1,5))
    blue.forward(randint(1,5))
    green.forward(randint(1,5))
    yellow.forward(randint(1,5))
    
