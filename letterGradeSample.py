###########################################################
# main                                                    #
#                                                         #
# Main function to control the program.                   #
# -Get test grade from user                               #
# -Determine the letter grade                             #
# -Show the results to the user                           #
###########################################################

def main():
    
 iTest = 0

 # 1. Prompt for test scores:
 iTest1 = promptForInteger("Enter a whole number 0 or greater: ")

 sLetterGrade = getLetterGrade(iTest1)

 # 2. Output the resuls:
 print("Test score:", iTest1, "is a:", sLetterGrade)
                 
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
             pass
             
    return iInput

###########################################################
# getLetterGrade                                          #
#                                                         #
# This code is alternative to code many if/elif/else      #
# statements. See if you can follow the code.  Then ask   #
# yourself what coding approach do you like best??        #
# -Receive an integer                                     #
# -Return a string letter grade                           #
###########################################################

def getLetterGrade(iGrade):

    sGrade = ""
    iDigit = 0

    # Determine the letter grade:
    iDigit = int(iGrade / 10)

    if iDigit >= 9 :
       sGrade = "A"
    elif iDigit == 8 :
       sGrade = "B"
    elif iDigit == 7 :       
       sGrade = "C"
    elif iDigit == 6 :       
       sGrade = "D"
    else :
       sGrade = "F"

    # Determine if + or - is needed:   
    if iGrade > 60 :
       iDigit = int(iGrade % 10)
       
       sGrade += "+" if iGrade >= 100 or iDigit >= 7 else "-"  if iDigit <= 3 else ""

    return sGrade;

main()


