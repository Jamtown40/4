# Compounding Interest with Loops
# Professor C.

# This code has 1 function prompt for:
# -Deposit must be positive value and non-zero
# -Interest must be positive value and non-zero
# -Number of Months must be positive value and non-zero
# -Goal must be positive value and zero is OK


#Created function to test input validation
# Parameter 1: Is the Prompt value that user will see on the screen
# Parameter 2: Indicates what the minimum value allowed is for example 0 or .01
def inputValidation(sPrompt, nMinNumberAllowed):

  # Testing user input with while loop displaying error message if invalid

  # Default fValue to -1 to force entry into the loop:
  fValue = -1

  # Keep Looping until a valid float that was >= to the Minimun Number that was supplied:
  while fValue < nMinNumberAllowed:
    try:
        fValue = float(input(sPrompt))
        if fValue <  nMinNumberAllowed:
            print ("Input must be a numeric value greater or equal to: ", nMinNumberAllowed)
            continue
    except ValueError:
            print ("Input must be a numeric value greater or equal to: ", nMinNumberAllowed)
            continue
          
  # If code reaches here a valid float numeric value that was > then the nMinNumberAllowed    
  return fValue

#Created function to calculate compounding interest
def MonthlyInterest(fDeposit,fInterestRate):
  return fDeposit * fInterestRate

#Main function asking for input(calling inputValidation and MonthlyInterest functions)
def main():

    fDeposit = inputValidation("What is the Original Deposit (positive value): ", 0.01)
    fInterestRate = inputValidation("What is the Interest Rate (positive value): ", 0.01)
    iMonths = int(inputValidation("What is the Number of Months (positive value): ", 0.01))
    fGoal = inputValidation("What is the Goal Amount (can enter 0 but not a negative):", 0.0)
    
#Calculating monthly interest  rate
    fMonthlyInterestRate = (fInterestRate/100)/12
    fAccountBalance = fDeposit

#Loop to output the month and monthly totals
    for iMonth in range(1, iMonths + 1):
      fAccountBalance += MonthlyInterest(fAccountBalance, fMonthlyInterestRate)
    
      print("Month: ", iMonth, "Account Balance is: $" + format(fAccountBalance, ",.2f"))

#Loop to calculate how long it would take to reach the goal set
    iMonth = 0
    fAccountBalance = fDeposit
    while fAccountBalance <= fGoal:
      fAccountBalance += MonthlyInterest(fAccountBalance, fMonthlyInterestRate)
      iMonth += 1
    
    print("It will take: ", iMonth, " months to reach the goal of $" + format(fGoal, ",.2f"))

#calling the main function
main()


