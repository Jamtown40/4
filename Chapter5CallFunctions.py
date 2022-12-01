
def main():

     iNumber = int(input("Enter a whole number: "))

     iDouble = doubleNumber(iNumber)
     print(iDouble)

     print(tripleNumber(iNumber))

def doubleNumber(iInput):
     return iInput * 2


def tripleNumber(iInput):
     return iInput * 3



main()
