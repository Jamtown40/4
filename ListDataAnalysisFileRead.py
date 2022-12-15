# Author: Prof. Candido
# This program will work with string and float 
# lists to experiement with data analysis.

import statistics


###############################################################
# readDataFromFile():                                         #
# Read the data from the file and place First Name and Salary #
# into a list and then return them:                           #
###############################################################
def readDataFromFile():

    sFirstNameFromFileList = []
    fSalaryFromFileList = []

    fileInput = open('ListDataAnalysisFileRead.txt', 'r')

    # Read the record and remove the new line character from the end:
    recInput = fileInput.readline()
    recInput = recInput.rstrip('\n')
    
    # Process each record in the file until there are no more:
    while recInput != '' :
        sFirstName = ""
        fSalary=0.0

        # Extract/Parse/Substring/Slice each fields
        sFields = recInput.split(',')
        
        # get first name:
        sFirstNameFromFileList.append(sFields[0])
        fSalary = float(sFields[1])
        fSalaryFromFileList.append(fSalary)
        
    
        # Read next record and remove the new line character from the end:
        recInput = fileInput.readline()
        recInput = recInput.rstrip('\n')

    # Close the file after exiting the loops:
    fileInput.close()

    # Return both lists to the main function:
    return sFirstNameFromFileList, fSalaryFromFileList


def main():
    
    sStudents, fSalary = readDataFromFile()


    print("Elements/entries:", len(sStudents) )
    print("Lowest value:", min(sStudents) )
    print("Lowest value:", max(sStudents)      )
    print("Value 2:", sStudents[2]      )

    print('---------------------------')    

    print("Elements/entries:", len(fSalary) )
    print("Lowest value:", min(fSalary) )
    print("Lowest value:", max(fSalary)      )
    print("Value 2:", fSalary[2]      )

    print("Attempt to sum:", sum(fSalary) )

    print("Attempt to avg:", sum(fSalary) / len(fSalary) )

    print("Attempt to avg:", statistics.mean(fSalary)  )

    print("Attempt to median:", statistics.median(fSalary)  )


main()


            
