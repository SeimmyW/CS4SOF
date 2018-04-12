#make a fuction that searches through a list

import random

#define some lists

section12A= [80, 75, 88, 80, 90, 77, 65]
section12B= [80, 75, 88, 80, 90, 77, 65]
section12C= [80, 75, 88, 80, 90, 77, 65]
section12D= [80, 75, 88, 80, 90, 77, 65]

def search(myList):
    found = False
    for i in range(len(myList)):
        if myList[i]==100:
            found=True
        print("The list contains a 100", found)

search(section12A)
