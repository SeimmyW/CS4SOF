# streaks of heads

import random

simNum = 0 # track # of simulations
countHeads = 0 # tracks how many flips were heads

while countHeads < 12:
    flip = random.randint(0,1)
    if flip == 1:
        countHeads = countHeads = countHeads + 1
    else:
        countHeads = 0
    print(flip)
    print("Heads Streak -", countHeads)
    simNum = simNum + 1

print("Total flips: ", simNum)
