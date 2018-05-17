#word scrambler description
while True:
    print("Welcome to the Word Scrambler")
    print("Choose Pig Latin, Flip, or Scramble, or Shift!")
    print("")
    print("")
    print("")
    user_input = input("What would you like to do? Pig Latin, Flip, Scramble, or Shift: ")

#the important stuff

    if user_input == "Pig Latin" or user_input == "pig latin" or user_input == "PIG LATIN":
        pyg ='ay'
        original = input("Enter a word: ")
        if len(original) and original.isalpha() > 0:
            word = original.lower()
            first = word[0]
            new_word = word[1:len(word)] + first + pyg
            print(new_word)
        else:
            print("Can't work. Try again.")
    if user_input == "Flip" or user_input == "flip" or user_input == "FLIP":
        while True:
            def reverse(string):
                return string[::-1]
            print(reverse(str(input("Enter a word:"))))
            break
    if user_input == "Scramble" or user_input == "scramble" or user_input == "SCRAMBLE":
        wrd = input("Enter a 8 letter word:")
        print(wrd[5], wrd[2], wrd[0], wrd[4], wrd[1], wrd[7], wrd[3], wrd[6],)
    if user_input == "Shift" or user_input == "shift" or user_input == "SHIFT":
        shifted = input("Enter a word to be shifted to the left: ")
        shiftnum = int(input("How many times are we shifting the word to the left? "))
        i = 0
        while i < shiftnum:
            x = 1
            shiftedword = []
            while x < len(shifted):
                shiftedword.append(shifted[x])
                x = x + 1
            shiftedword.append(shifted[0])
            shifted = shiftedword
            i = i + 1
        print(shifted)
    print("")
    print("")
    print("")
    userinput = input("Would you like to play again? Y/N: ")
    if userinput == "Y" or userinput == "y":
        continue
    else:
        break
