#Finds the final balance of compound interest based on values given by user
#Seim Wolderufael 12B 12/20/2017
balance = float(input("Initial Balance: "))
rate = float(input("Interest Rate: "))
years = int(input("Number of years: "))
finalbalance = balance * (1 + rate) ** years
print("Final balance:", finalbalance)
