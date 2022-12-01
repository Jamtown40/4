
# Working with Global parameters/arguments

# To MAKE GLOBAL Variables you MUST:
# 1. Declare the variables at the top of the program
# 2. In every FUNCTION you want to access and/or change add the keyword
#    global in front of the variable.  
# 3. Do not assign the value on the same line as the global keyword.  Do
#    that on a separate line. 

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

     # Add the keyword global to make these variables access
     # the variables declared on lines 3 and 4 and not make them
     #local variables: 
     global sFirst
     global sLast 

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

