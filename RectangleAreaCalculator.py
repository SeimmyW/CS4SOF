while True:
    print("This program finds the area of a rectangle.")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("The area is: ", length * width)
    contcondition = input("Do you want to continue? (Type Yes or No): ")
    if contcondition != "Yes":
        print("Goodbye!")
        break
    else:
        continue
    
