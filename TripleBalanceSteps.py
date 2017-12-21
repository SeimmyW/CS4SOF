# step 1 initial variables, constants

INITIAL_BALANCE = 800
TARGET_BALANCE = INITIAL_BALANCE * 3
RATE = 3.0

# step 2 initialize variables used with this loop

balance = INITIAL_BALANCE
year = 0

# step 3, count the years required for the investment to triple

while balance <TARGET_BALANCE:
    year = year + 1
    interest = balance*RATE/100
    balance = balance + interest

# step 4, print the results

print("The investment tripled after", year, "years.")
