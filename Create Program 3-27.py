#source1: https://docs.python.org/3.3/library/turtle.html
import turtle

def PenOptions():
    colorchoice = input("Choose a color (red, yellow, orange, green, blue, purple, black) ")
    turtle.pen(fillcolor="black", pencolor=colorchoice, pensize=1)
    newpensize = int(input("Choose a pensize "))
    turtle.pen(pensize = newpensize)
    DrawingLines()
    
def DrawingLines():
    i = 0
    howmanylines = int(input("Type the number of lines you want to create "))
    while i < howmanylines:
        print("Options for line", i + 1, "of", howmanylines)
        angle = int(input("Type the integer for the Angle of the Line "))
        linelength = int(input("Type the integer for the Length of the Line "))
        turtle.right(angle)
        turtle.forward(linelength)
        i = i + 1
    UserChoice()

def UserChoice():
    continuing = input("Type makemore if you want to make more lines, menu for pen options, or quit to leave the program: ")
    if continuing == "makemore":
       DrawingLines()
    if continuing == "menu":
       PenOptions()
    if continuing == "quit":
        print("Goodbye :)")
    else:
        print("Invalid Choice")
        UserChoice()
        

angle = 0
linelength = 0
howmanylines = 0
print("-------------------------------------------------------------------------")
print("INSTRUCTIONS")
print("Welcome to the Turtle Type-To-Draw!")
print("1. Choose a color")
print("2. Choose a pensize")
print("3. Choose the number of lines you want to draw")
print("4. Type an integer for the (clockwise) angle and press return")
print("5. Type an integer for the length of the line")
print("-------------------------------------------------------------------------")
PenOptions()
turtle.pen(fillcolor="black", pencolor="red", pensize=10)
    
