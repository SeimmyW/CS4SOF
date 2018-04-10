#simulate a coin flip 10 times

import random

#track the number of simulations
# 1 = head, 0= tails

simNum = 0
flip = random.randint(0,1)
countHeads = 0

while simNum<10:
        if flip ==1:
        print("head - ", end="")
        countHeads = countHeads + flip
        print(countHeads)
    print(flip)
    flip = random.randint(0,1)
    simNum =simNum + 1
    
print("10 tries done")
    
