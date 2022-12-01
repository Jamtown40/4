# This program demonstrates how to read data from a file
# It will parse out each field

def main():

    fileInput = open('FileReadSample.txt', 'r')

    # Read the record and remove the new line character from the end:
    recInput = fileInput.readline()
    recInput = recInput.rstrip('\n')

    # Put headings out:
    print("Entire records:")
    
    # Process each record in the file until there are no more:
    while recInput != '' :
        print(recInput)
    
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
