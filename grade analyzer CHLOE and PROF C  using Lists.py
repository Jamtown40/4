#Author: Prof. C and Chloe Gerhardson
#Grade Analyzer Version 2 --> Using Lists

#Gather name, get inputs for four test scores

sName = input("Name of person that we are calculating the grades for:")
iTestScore1 = int(input("Test 1:"))
iTestScore2 = int(input("Test 2:"))
iTestScore3 = int(input("Test 3:"))
iTestScore4 = int(input("Test 4:"))
iTestScore5 = int(input("Test 5:"))
iTestScore6 = int(input("Test 6:"))
iTestScore7 = int(input("Test 7:"))

iTests = [iTestScore1,iTestScore2,iTestScore3,iTestScore4,iTestScore5,iTestScore6,iTestScore7]


#Compute average with or without lowest test score.
for iGrade in iTests:
    if iGrade < 0:
        exit(print("Test scores must be greater than 0"))


#Ask if the user wants to drop their lowest test score.
sTestDrop = input("Do you wish to drop the Lowest Grade [Y] or [N]?")

if sTestDrop != "Y" and sTestDrop != "N":
    exit(print("Enter 'Y' or 'N' to Drop the Lowest Grade"))
    
iLow = 0
iTest = len(iTests)

if sTestDrop.upper() == "Y":
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



