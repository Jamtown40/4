
# Working with Global parameters/arguments

# Look at the code below and see if it will work???

# Set a value up here at the top so the entire program can
# access, change and use the values:
sFirst = ""
sLast = ""


def printName():
     # Make these variables that were declared at the top
     # but we can change the value here:
     global sFirst
     global sLast
     
     print("From within the printName() First Name: ", sFirst, " Last Name: ", sLast)

     # Change the values here within the printName()
     sFirst = "Moose"
     sLast = "Candido"
     

def main():
     sFirst = input("What is your First name: ")
     sLast = input("What is your Last name: ")

     #Pass arguments by position correctly and
     #the values will change within the printName() function
     printName()

     # After coming back from the printName() function see how the value
     # changed:
     print("From within the main() First Name: ", sFirst, " Last Name: ", sLast)

# Call the main() function:
main()

