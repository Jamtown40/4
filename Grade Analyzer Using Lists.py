# This program will determine the average of a set of test scores and drop
# the lowest grade should dependent on user input.

# Prompt user for input and convert
sSubject = input("Name of the person that we are calculating grades for: ")
fT1 = float(input("Test 1: "))
fT2 = float(input("Test 2: "))
fT3 = float(input("Test 3: "))
fT4 = float(input("Test 4: "))
sDrop = input("Do you wish to drop the lowest grade('Y' for yes and 'N' for no): ")

# Use an if statement to test if input is valid
if fT1 < 0 or fT2 < 0 or fT3 < 0 or fT4 < 0:
    print("Test scores must be greater than 0")
    exit()

# Determine the average of the scores dependent on user's input.
fListGrades = [fT1,fT2,fT3,fT4]

# Dependent on user input the lowest sccore may or may not be dropped
if sDrop == "Y" or sDrop == "y":
    fLowest = min(fListGrades)
    iNumberOfTests = 3
elif sDrop == "N" or sDrop == "n":
    fLowest = 0
    iNumberOfTests = 4
else:
    print("You must enter a Y or N")
    exit()

# Determine the average:
print("Debug:" , sum(fListGrades) ,  min(fListGrades) , iNumberOfTests)
fAverage = (sum(fListGrades) - fLowest) / iNumberOfTests
print(sSubject, "'s test average is ",format(fAverage,"0.1f"))
    
# The if statments test to see what range the average score falls under and
# displays a letter grade associated with that range
if fAverage >= 97.0:
    print("Letter grade for the test is: A+")
elif fAverage >= 94.0 :
    print("Letter grade for the test is: A")
elif fAverage >=90.0 :
    print("Letter grade for the test is: A-")
elif fAverage >= 87.0 :
    print("Letter grade for the test is: B+")
elif fAverage >= 84.0 :
    print("Letter grade for the test is: B")
elif fAverage >= 80.0 :
    print("Letter grade for the test is: B-")
elif fAverage >= 77.0 :
    print("Letter grade for the test is: C+")
elif fAverage >= 74.0 :
    print("Letter grade for the test is: C")
elif fAverage >= 70.0 :
    print("Letter grade for the test is: C-")
elif fAverage >=67.0 :
    print("Letter grade for the test is: D+")
elif fAverage >= 64.0 :
    print("Letter grade for the test is: D")
elif fAverage >= 60.0 :
    print("Letter grade for the test is: D-")
else:
    print("Letter grade for the test is: F")
    

