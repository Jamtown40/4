# By:      Professor Brian Candido
# Purpose: This program calculates the averages for 4 test
#          Has logic to drop the lowest grade
#          And display the results and a letter grade

#          Updated to use functions




def main():

 iDivisor = 3
 iLowest = 0

 # 1. Prompt for test scores:
 iTest1 = promptForInteger("Enter Test 1 Score: ")
 iTest2 = promptForInteger("Enter Test 2 Score: ")
 iTest3 = promptForInteger("Enter Test 3 Score: ")

 sInput = input("Drop Lowest Grade Y or N:")


 # 2. Calculate:

 # 2.1 Determine if to drop the lowest grade:
 if sInput == "Y":
     iLowest = minNumber(iTest1, minNumber(iTest2, iTest3))
     iDivisor = 2

 # 2.2 Calculate the grade:
 fAverage = (iTest1 + iTest2 + iTest3 - iLowest) / iDivisor
    
 # 2.3 Get the Letter grade: 
 
 sLetterGrade = getLetterGrade(fAverage)
 
 # 3. Output
 print('Test average is: ', fAverage)
 print('Letter Grade is: ' +  sLetterGrade )


###########################################################
# getLetterGrade                                          #
#                                                         #
# Recieve a number that contains the Average and return   #
# a String with the letter grade.                         #
###########################################################


def getLetterGrade(fGrade):

    if  fGrade >= 90.0 :
        sLetterGrade = "A"
    elif  fGrade >= 80.0 :
        sLetterGrade = "B"
    elif  fGrade >= 70.0 :
        sLetterGrade = "C"
    elif  fGrade >= 60.0 :
        sLetterGrade = "D"
    else: 
        sLetterGrade = "F"

    # Check if a + or - is needed on the Letter Grade:

    if fGrade >= 60 :
        # Get the right most digit:
        iFirstDigit = int(fGrade % 10)
        if iFirstDigit >= 7 or fGrade >= 100:
            sLetterGrade += '+'
        elif iFirstDigit <= 3:
            sLetterGrade += '-'

    return sLetterGrade
    

###########################################################
# min                                                     #
#                                                         #
# Recieve 3 numbers and return the lowest value of the 3  #
###########################################################

            
def minNumber(iNumber1, iNumber2):

    return  iNumber1 if iNumber1 < iNumber2 else iNumber2

    # or Python has min function built in that you can use:
    #return min(iNumber1, iNumber2)

                
###########################################################
# promptForInteger                                        #
#                                                         #
# Ask the user for an integer and make sure the following #
# -Numeric value                                          #
# -Between 0 and 100                                      #
###########################################################


def promptForInteger(sPromptMessage):
    iInput = -1
    
    while iInput < 0:
    
        try:
            iInput = int(input(sPromptMessage))
        except ValueError:
             print("Input must a number.")
             
    return iInput


main()


 

   
    



