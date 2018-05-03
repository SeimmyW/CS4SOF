def namecheck(name):
    if name != "Red":
        if name != "Blue":
            if name != "Green" :
                if name != "Yellow":
                    raise Exception('Invalid Color Choice!')
                else:
                    print("Yellow is ok I guess..")
            else:
                print("Green is icky!")
        else:
            print("Blue is a second choice for me") 
    else:
        print("I also like red the best!")
             
name = input("Which color do you like best: Red, Blue, Green, Yellow \n")
try:
    namecheck(name)
except Exception as err:
    print('An exception happened: ' + str(err))
