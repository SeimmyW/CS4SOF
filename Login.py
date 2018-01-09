print("Welcome to Gmail")
myUsername = input("Enter your username, then press return: ")

if myUsername == "johndoe":
    print("Username successful")
    myPassword = input("Enter your password, then press return: ")
    if myPassword=="sof1230":
        print("Success!")
    else:
        print("Unable to log in. Incorrrect password")
else:
    print("Incorrect. Try Again")
