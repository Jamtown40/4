fNumber = float( input("Enter a floating point value with several decimals: "))

#Show the user the value unformatted
print("The value is: ", fNumber)

#Show the user the value formatted
print("The value formatted is: ", format(fNumber, '.2f'))
      
# This code will remove all extra decimal points up after the first decimal point
fNumber2 = round(fNumber,1)
print("The value rounded to 1 decimal is: ", fNumber2)
