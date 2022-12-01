# By:      Professor Brian Candido
# Purpose: This program calculates the averages for 3 test
#          Has logic to drop the lowest grade
#          And display the results and a letter grade


iDivisor = 3
iLowest = 0

# 1. Prompt for test scores:

iTest1 = int(input("Test 1: ") )
iTest2 = int(input("Test 2: ") )
iTest3 = int(input("Test 3: ") )


sDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ")

    
# 2. Calculate:

# 2.1 Determine if to drop the lowest grade:
if sDropLowest == 'Y':
   iDivisor = 2

   if   iTest1 < iTest2 and iTest1 < iTest3 :
        iLowest = iTest1
   elif iTest2 < iTest3 :
        iLowest = iTest2
   else:
        iLowest = iTest3

# 2.2 Calculate the grade:
fAverage = (iTest1 + iTest2 + iTest3 - iLowest) / iDivisor

# 2.3 Get the Letter grade:
if  fAverage >= 97.0 :
        sLetterGrade = "A+"
elif  fAverage >= 94.0 :
        sLetterGrade = "A"
elif  fAverage >= 90.0 :
        sLetterGrade = "A-"
elif  fAverage >= 87.0 :
        sLetterGrade = "B+"
elif  fAverage >= 84.0 :
        sLetterGrade = "B"
elif  fAverage >= 80.0 :
        sLetterGrade = "B-"
elif  fAverage >= 77.0 :
        sLetterGrade = "C+"
elif  fAverage >= 74.0 :
        sLetterGrade = "C"
elif  fAverage >= 70.0 :
        sLetterGrade = "C-"
elif  fAverage >= 67.0 :
        sLetterGrade = "D+"
elif  fAverage >= 64.0 :
        sLetterGrade = "D"
elif  fAverage >= 60.0 :
        sLetterGrade = "D-"
else: 
        sLetterGrade = "F"
	      

# 3. Output: 
print('Test average is: ',  fAverage)
print('Letter Grade for the test is: ' +  sLetterGrade )





