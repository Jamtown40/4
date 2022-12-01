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
     iLowest = minNumber(iTest1, iTest2, iTest3)
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

    if  fGrade >= 97.0 :
        sLetterGrade = "A+"
    elif  fGrade >= 94.0 :
        sLetterGrade = "A"
    elif  fGrade >= 90.0 :
        sLetterGrade = "A-"
    elif  fGrade >= 87.0 :
        sLetterGrade = "B+"
    elif  fGrade >= 84.0 :
        sLetterGrade = "B"
    elif  fGrade >= 80.0 :
        sLetterGrade = "B-"
    elif  fGrade >= 77.0 :
        sLetterGrade = "C+"
    elif  fGrade >= 74.0 :
        sLetterGrade = "C"
    elif  fGrade >= 70.0 :
        sLetterGrade = "C-"
    elif  fGrade >= 67.0 :
        sLetterGrade = "D+"
    elif  fGrade >= 64.0 :
        sLetterGrade = "D"
    elif  fGrade >= 60.0 :
        sLetterGrade = "D-"
    else: 
        sLetterGrade = "F"

    return sLetterGrade
    

###########################################################
# min                                                     #
#                                                         #
# Recieve 3 numbers and return the lowest value of the 3  #
###########################################################

            
def minNumber(iNumber1, iNumber2, iNumber3):

    iLowest = 0
    
    if iNumber1 <= iNumber2 and iNumber1 <= iNumber3:
        iLowest = iNumber1
    elif iNumber2 <= iNumber3:
       iLowest = iNumber2
    else:
       iLowest = iNumber3
             
    return iLowest    
                
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


 

   
    



