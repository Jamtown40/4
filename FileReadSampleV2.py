# This program demonstrates how to read data from a file

# It will parse out each field

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
        fSalary = float(sSalary)

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

# Program starting point:
main()
