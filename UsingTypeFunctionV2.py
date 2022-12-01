
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
def main():

    while True:
        sInput = input("Enter a value (can be a int, float or a string (q to quit): ")
        if sInput == "q":
            break
        sDataType = getDataType(sInput)
        print("You entered: ", sInput, "is this data type", sDataType)

        
        
main()
