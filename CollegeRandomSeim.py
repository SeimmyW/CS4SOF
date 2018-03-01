# write a program that returns random choices to the user
import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return "NYU"
    elif answerNumber==2:
        return "Stony Brook"
    elif answerNumber==3:
        return "University Of Phoenix"
    elif answerNumber==4:
        return "BMCC"
    elif answerNumber==5:
        return "Hamburger University"
    elif answerNumber==6:
        return "Dropout"
    elif answerNumber==7:
        return "Held Back"
    elif answerNumber==8:
        return "Massachutses Institute of Technology"
    elif answerNumber==9:
        return "Hostos"
    elif answerNumber==10:
        return "Havard College"

tries= 0

while tries<10:
    userInput= input("What college willl I go to ")
    if userInput=="1":
        print(getAnswer(random.randint(1,10)))
        tries = tries + 1
    elif userInput=="2":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="3":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="4":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="5":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="6":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="7":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="8":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="9":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
    elif userInput=="10":
        print(getAnswer(random.randint(1,10)))
        tries = tries+ 1
