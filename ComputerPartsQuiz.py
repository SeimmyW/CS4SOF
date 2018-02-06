# Trivia Quiz

print("This is a quiz that will test your knowledge on computer parts")

name = input("Enter your name: ")
print("Hi, there,", name, "Are you ready for the quiz?")

print("I will ask you 6 questions and give you three choices")
print("Select which choice is the correct answer, A, B, or C")

# set the score of the quiz to 0
score = 0
score = int(score)

#question 1
print("")
print("Question 1: Which one of these companies DOES NOT make processors?")
print("")
print("A. Intel")
print("B. Cooler Master")
print("C. Advanced Micro Devices")
print("")

Q1answer="B" # the right answer to question 1
Q1response = input("Your answer: ")

if Q1response == "B" or Q1response == 'b':
    print("Correct answer", Q1answer)
    score = score+1
elif Q1response != "B" and Q1response != 'b':
    print("Sorry, incorrect")

print("Your current score is ", score, "out of 6")

#question 2
print("")
print("Question 2: Which computer part handles 3d applications and video?")
print("")
print("A. RAM")
print("B. PSU")
print("C. GPU")
print("")

Q2answer="C" # the right answer to question 2
Q2response = input("Your answer: ")

if Q2response == "C" or Q2response == 'c':
    print("Correct answer", Q2answer)
    score = score+1
elif Q2response != "C" and Q2response != 'c':
    print("Sorry, incorrect")

print("Your current score is ", score, "out of 6")

#question 3
print("")
print("Question 3: What are the pixel dimensions of 8k resolution?")
print("")
print("A. 7680*4320")
print("B. 8000*4000")
print("C. 7580*4400")
print("")

Q3answer="A" # the right answer to question 3
Q3response = input("Your answer: ")

if Q3response == "A" or Q3response == 'a':
    print("Correct answer", Q3answer)
    score = score+1
elif Q3response != "A" and Q3response != 'a':
    print("Sorry, incorrect")

print("Your current score is ", score, "out of 6")


#question 4
print("")
print("Question 4: What computer part connects the various parts together?")
print("")
print("A. CPU")
print("B. Keyboard")
print("C. Motherboard")
print("")

Q4answer = "C" # the right answer to question 4
Q4response = input("Your answer: ")

if Q4response == "C" or Q4response == 'c':
    print("Correct answer", Q4answer)
    score = score+1
elif Q4response != "C" and Q4response != 'c':
    print("Sorry, incorrect")

print("Your current score is ", score, "out of 6")

#question 5
print("")
print("Question 5: Which event hosts new technological innovations?")
print("")
print("A. E3")
print("B. SXSW")
print("C. CES")
print("")

Q5answer = "C" # the right answer to question 5
Q5response = input("Your answer: ")

if Q5response == "C" or Q5response == 'c':
    print("Correct answer", Q5answer)
    score = score+1
elif Q5response != "C" and Q5response != 'c':
    print("Sorry, incorrect")

#question 6
print("")
print("Question 6: Which standard has the fastest transfer rate?")
print("")
print("A. USB 3.0")
print("B. Thunderbolt")
print("C. SATA")
print("")

Q6answer = "B" # the right answer to question 6
Q6response = input("Your answer: ")

if Q6response == "B" or Q6response == 'b':
    print("Correct answer", Q6answer)
    score = score+1
elif Q6response != "B" and Q6response != 'b':
    print("Sorry, incorrect")

# percentage score

final_score = (score*100)/6
print("You got", score, "out of 6")
print("This is a score of " +str(final_score)+ " percent")
