#processing and manipulating lists

import random

lotteryNumbers = []

lotteryNumbers.append(random.randint(1,70))
lotteryNumbers.append(random.randint(1,70))
lotteryNumbers.append(random.randint(1,70))
lotteryNumbers.append(random.randint(1,70))
lotteryNumbers.append(random.randint(1,70))
lotteryNumbers.append(random.randint(1,70))

print(lotteryNumbers)

for i in range(0, len(lotteryNumbers)):
    print(lotteryNumbers[i])

# modify the list to add 5 to every value in the list

for i in range(0, len(lotteryNumbers)):
    lotteryNumbers[i] = lotteryNumbers[i] + 5
    print(lotteryNumbers[i])
