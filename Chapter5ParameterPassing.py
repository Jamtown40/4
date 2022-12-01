
# Working with Keyword parameters/arguments


def printName(sFirst, sLast):
     print("First Name: ", sFirst, " Last Name: ", sLast)
     


sName1 = input("What is your First name: ")
sName2 = input("What is your Last name: ")

#Pass arguments by position correctly
printName(sName1, sName2)

#Pass arguments by position incorrectly
printName(sName2, sName1)

#Pass arguments in any order by matching using the =
printName(sLast = sName2, sFirst = sName1)
