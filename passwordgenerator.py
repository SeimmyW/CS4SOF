import random

print("Welcome to the random password generator!")
passwordlength = int(input("Please enter the desired password length\n"))
howmanypasswords = int(input("How many passwords do you want to generate?\n"))
x = 0
password = ""
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','&','$','#','@','!','%','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while x < howmanypasswords:
    y = 0
    while y < passwordlength:
        password = password + random.choice(chars)
        y = y + 1
    print(password)
    password = ""
    x = x + 1
if passwordlength < 4:
    print("Your password/s are weak. You need to make it longer.")
if passwordlength >= 4:
    if passwordlength < 8:
        print("Your password/s has medium strength. You should make it longer.")
if passwordlength >= 8:
    print("Your password/s are strong.")
