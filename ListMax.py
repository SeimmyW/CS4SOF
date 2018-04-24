testScores = [77.7, 88.5, 99, 81.5, 86, 88, 78, 65, 67, 93]

def findMaxVal(testScores):
    print("Original values: ", testScores)
    maxVal = 0
    for i in range(0, len(testScores)):
        if testScores[i] > maxVal:
            maxVal = testScores[i]
    print("The maximum value in the list is: ", maxVal)

(findMaxVal(testScores))
    
    
