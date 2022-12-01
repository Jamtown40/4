# Author: Prof. Candido
# Check out this coding solution and see why you don't want to use it!

def main():

    # Embedded Funtion
    def doubleNumber(fInNumber):
        
        return fInNumber * 2

    # Ask for Input:
    fNumber1  = float(input("Enter a number to double: "))

    # Call the doubleNumber function from within the main():
    fResult = doubleNumber(fNumber1)
    print("Double value: ", fResult)
    
    print("Triple value: ", tripleNumber(fNumber1))

# Function declared OUTSIDE of other functions so it sharable/accessible
# from all parts of the program:

def tripleNumber(fInNumber):
        
    return fInNumber * 3


# Call the main function    
main()

# Try accessing the doubleNumber() function:
print("Double value: ", doubleNumber(14))
