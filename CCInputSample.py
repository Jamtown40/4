
# main function
def main():

    inputFile = open('PythonCodeCamp04172020.txt', 'r')

    recInput = inputFile.readline()
    recInput = recInput.rstrip('\n')
    iRecord = 0
    
    # Process each record in the file until there are no more:
    while recInput != '' :
      iRecord += 1
      print("Record:", iRecord, "Value is:",recInput)
      recInput = inputFile.readline()
      recInput = recInput.rstrip('\n')

    # close the file. But NOT in the LOOP  
    inputFile.close()


# Call the main function.
main()


