miles = int(input("Miles travelling: "))
mpg = int(input("How many miles can be travelled in one gallon: "))
mpg = 1/mpg
gallonprice = float(input("Price per gallon: "))
price = miles * mpg * gallonprice
print("Cost of fuel: " , price)
