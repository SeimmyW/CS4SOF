print("Calculate your compound interest growth: ")
balance = float(input("Initial balance: "))
interest = float(input("Interest (in %): "))
year = int(input("Number of years: "))

for i in range (year):
    balance = balance * (1 + interest)
    print("Year", i+1, 'has a balance of %.2f' % (balance))

