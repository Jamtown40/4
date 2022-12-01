# Author: Brian Candido
# Purpose: Force certain Python data types as a parameter values:


# Force for specific data types on the incoming parameters and
# notify a float is returned:
def getFloatInput(sPrompt: str, fMinAllowedValue: float) -> float:
    while True:
        try:
             nUserInput = float(input(sPrompt))
        except ValueError:
            print("Not a valid number! Please try again.")
            continue
        # You can add an else to a try/except to go if the except is NOT executed  
        else:
            if nUserInput < fMinAllowedValue:
                print("Entry must be greater than or equal to", fMinAllowedValue, ". Please try again.")
                continue
            else:
                return nUserInput


def main():

  # Will work: 
  fNumber = getFloatInput("Enter a number: ", 0)
  print("You entered a number and it now a float! ", fNumber)

  # Will not work because BC can't be converted to float that
  # is expected as the second parameter
  fNumber = getFloatInput("Enter a number: ", "blc")
  print("You entered a number and it now a float! ", fNumber)


  

main()



