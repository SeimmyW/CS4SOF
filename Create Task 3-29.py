#source1: https://docs.python.org/3.3/library/turtle.html
import turtle

def PenOptions():
    colorchoice = input("Choose a color (red, yellow, orange, green, blue, purple, black): \n")
    turtle.pen(fillcolor="black", pencolor=colorchoice, pensize=1)
    newpensize = int(input("Choose a pensize: \n"))
    turtle.pen(pensize = newpensize)
    DrawingLines()
    
def DrawingLines():
    i = 0
    howmanylines = int(input("Type the number of lines you want to create: \n"))
    while i < howmanylines:
        print("-------------------------------------------------------------------------")
        print("LINE", i + 1, "OF", howmanylines)
        angle = int(input("Type the integer for the Angle of the Line: \n"))
        linelength = int(input("Type the integer for the Length of the Line: \n"))
        turtle.right(angle)
        turtle.forward(linelength)
        i = i + 1
        print("-------------------------------------------------------------------------")
    UserChoice()

def UserChoice():
    
    continuing = input("End Commands:\n -makemore if you want to make more lines \n -menu for pen options \n -reset to reset turtle \n -quit to leave the program: \n ")
    if continuing == "makemore":
       DrawingLines()
    if continuing == "menu":
       PenOptions()
    if continuing == "reset":
        turtle.reset()
        PenOptions()
    if continuing == "quit":
        print("Goodbye :)")
    if continuing != "makemore":
        if continuing != "menu":
            if continuing != "reset":
                if continuing != "quit":
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
