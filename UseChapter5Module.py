# Prof. Candido
# Sample using the Chapter5Module.py module:

import Chapter5Module

def main():
     # Ask for 2 int numbers and then find the smallest,largest, average and sum:
     iNumber1 = int(input("Enter an int for a Number 1: "))
     iNumber2 = int(input("Enter an int for a Number 2: "))

     print("The smallest number is: ", Chapter5Module.min_number(iNumber1, iNumber2))
     print("The biggest number is: ", Chapter5Module.max_number(iNumber1, iNumber2))
     print("The average is: ", Chapter5Module.avg_numbers(iNumber1, iNumber2))
     print("The sum is: ", Chapter5Module.sum_numbers(iNumber1, iNumber2))
     
     
     # Ask for 2 float numbers and then find the smallest,largest, average and sum:
     fNumber1 = float(input("Enter a float for a Number 1: "))
     fNumber2 = float(input("Enter a float for a Number 2: "))

     print("The smallest number is: ", Chapter5Module.min_number(fNumber1, fNumber2))
     print("The biggest number is: ", Chapter5Module.max_number(fNumber1, fNumber2))
     print("The average is: ", Chapter5Module.avg_numbers(fNumber1, fNumber2))
     print("The sum is: ", Chapter5Module.sum_numbers(fNumber1, fNumber2))

# Call the main() function:   
main()
