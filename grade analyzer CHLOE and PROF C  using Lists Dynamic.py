#Author: Chloe Gerhardson & Prof. C
#Grade Analyzer Version 3 --> Using Dynamic Lists

iTests = []

#Gather name, get inputs for four test scores

sName = input("Name of person that we are calculating the grades for:")
iTestEntered = 0
iTestCounter = 1
while iTestEntered > -1 :
    iTestEntered = int(input("Enter Test: " + str(iTestCounter) + " score numeric values only (-1 to exit): "))
    if iTestEntered < 0:
        break
    iTests.append(iTestEntered)
    iTestCounter += 1

#Ask if the user wants to drop their lowest test score.
sTestDrop = input("Do you wish to drop the Lowest Grade [Y] or [N]?")

if sTestDrop != "Y" and sTestDrop != "N":
    exit(print("Enter 'Y' or 'N' to Drop the Lowest Grade"))
    
iLow = 0
iTest = len(iTests)

if sTestDrop == "Y":
    iTest -= 1
    iLow = min(iTests)    

sAverage = (sum(iTests) - iLow) / iTest

#Analyze Letter Grade and display Average, and Letter Grade to user.

sGrade = "A+" if sAverage >= 97 else "A" if sAverage >= 94 else "A-" if sAverage >= 90 else "B+" \
         if sAverage >= 87 else "B" if sAverage >= 84 else "B-" if sAverage >= 80 else "C+" \
         if sAverage >= 77 else "C" if sAverage >= 74 else "C-" if sAverage >= 70 else "D+" \
         if sAverage >= 67 else "D" if sAverage >= 64 else "D-" if sAverage >= 60 else "F" 

print(sName, "'s test average is:", format(sAverage, ".1f"))
print("Letter Grade for the test is:", sGrade)



