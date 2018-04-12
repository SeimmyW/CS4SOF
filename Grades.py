# look for a value on a list to see if it's there
# build a function to search for any value in a list

import random

randomGrades=[]

for i in range(0,10):
    randomGrades.append(random.randint(55,100))

print("Original", randomGrades)

for i in range(0, len(randomGrades)):
    if randomGrades[i]>=90:
        print(randomGrades[i], "You are in the Honors")
    elif randomGrades[i] >= 75:
        print(randomGrades[i], "You are Passing Well")
    elif randomGrades[i] >= 65:
        print(randomGrades[i], "You are borderline")
    else:
        print(randomGrades[i], "Have fun at Summer school")

#display a value in the list
for i in range(0,len(randomGrades)):
    if randomGrades[i]==85:
        print(True)
        print(randomGrades[i])

def search():
    found = False
    for i in range(0, len(randomGrades)):
        if randomGrades[i]==90:
            found=True
        print("The list of grades includes a 90", found)
        
