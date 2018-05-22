import random

print("Welcome to the random password generator!")
x = 0
password = ""
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','&','$','#','@','!','%','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while x < 8:
    password = password + random.choice(chars)
    x = x + 1
print(password)
