# This program demonstrates how to read data from a file and
# includes code to make sure the values are in fact a number before
# it attempts to convert to a float. 

def main():

    fileInput = open('FileReadSample.txt', 'r')

    # Read the record and remove the new line character from the end:
    recInput = fileInput.readline()
    recInput = recInput.rstrip('\n')

    # Put headings out:
    outputLine("First Name", "Last Name", "Salary", False)
    
    # Process each record in the file until there are no more:
    while recInput != '' :
        iBegin = 0
        iEnd = 0
        sFirstName = ""
        sLastName= ""
        fSalary=0.0

        # Extract/Parse/Substring/Slice each fields

        # get first name:
        iEnd = recInput.index(',')
        sFirstName = recInput[iBegin: iEnd]

        # get Last name:
        iBegin = iEnd + 1
        iEnd = recInput.index(',' , iBegin)
        sLastName = recInput[iBegin: iEnd]

        #Get Salary from after the last , and to the end of the string contents:
        iBegin = iEnd + 1
        sSalary = recInput[iBegin:]

        # Convert it from string to a float:

        sDataType = getDataType(sSalary)
        if sDataType == 'int' or sDataType == 'float':
           fSalary = float(sSalary)
        else:
            fSalary = 0

        #Output the three separate fields with defined spacing:
        outputLine(sFirstName, sLastName, fSalary, True)
    
        # Read next record and remove the new line character from the end:
        recInput = fileInput.readline()
        recInput = recInput.rstrip('\n')

    # Close the file after exiting the loops:

    fileInput.close()


def outputLine(sField1, sField2, sField3, blnFormatLastFieldAsNumeric):

    if blnFormatLastFieldAsNumeric :
        print('{:12}'.format(sField1) + '{:12}'.format(sField2) + '{:10,.2f}'.format(sField3) )
    else:
        print('{:12}'.format(sField1) + '{:13}'.format(sField2) + '{:12}'.format(sField3) )

# This is very cool code that I wrote for you.
# I am going to assemble these into a module :)
def getDataType(sToCheck):
    try:
        # if both the same the number is an int
        if int(sToCheck) == float(sToCheck):
            return 'int'
    except:
       # if not int check to see if it is a float:
       try:
            float(sToCheck)
            return 'float'
       # it must a string: 
       except:
            return 'str'


# Program starting point:
main()
