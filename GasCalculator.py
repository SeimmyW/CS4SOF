while True:
    print("This program calculates mpg.")
    milesDriven = float(input("Enter the milesDriven: "))
    gallonsUsed = float(input("Enter the Amount of Gallons Used: "))
    mpg = milesDriven / gallonsUsed
    print("Miles per gallon:", mpg)
    contcondition = input("Do you want to continue? (Type Yes or No): ")
    if contcondition != "Yes":
        print("Goodbye!")
        break
    else:
        continue


