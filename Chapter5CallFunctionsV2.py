
def main():

     iNumber = int(input("Enter a whole number: "))

     iDouble = doubleNumber(iNumber)
     print(iDouble)

     print(tripleNumber(iNumber))

     iDouble, iTriple = doubleAndTriple(iNumber)
     print(iDouble, iTriple)

def doubleNumber(iInput):
     return iInput * 2


def tripleNumber(iInput):
     return iInput * 3

def doubleAndTriple(iNumber):
     return doubleNumber(iNumber), tripleNumber(iNumber)



main()
