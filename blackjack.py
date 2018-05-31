import random

name = input("Please enter your name")
print("Welcome to the BlackJack game.")
print("Game rules:")
print("The player and the dealer recieve two cards from a shuffled deck. You need to make 21 to beat the dealer and win BlackJack.")
print("----------")
print("If the sum of your two numbers is higher than the dealers and add up to 21, then you won the BlackJack.")
print("----------")
print("If both you and the dealer are at 21, then it's a tie.")
print("----------")
print("Whoever has the highest number under 21 wins.")
print("----------")
print("Whoever has the number above 21, looses the round.")
print("----------")
print("Ready? Hit Enter/Return to start:")
nothing = input()
cards = ["A", "A", "A", "A", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"]
playershand = []
dealershand = []

#def ACheck():
    #seperate A from other strings
    #if seperate A plus other values is > 21
    #Make A = 1
x=0
while x < 2:
    dealershand.append(random.choice(cards))
    x = x + 1
print("Dealer's Hand:", dealershand)
x=0
while x < 2:
    playershand.append(random.choice(cards))
    x = x + 1
print("Player's Hand: ", playershand)

    
