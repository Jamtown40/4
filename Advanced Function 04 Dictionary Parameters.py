# Author: Brian Candido
# Purpose: Python dictionary as a parameter values:

# put a ** in front of the variable to denote a dictionary parms:

#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_dictionary_parameters_function(**sKid):
  print("Person's last name is " + sKid["lname"])



def main():

  # My own family: 
  my_dictionary_parameters_function(fname = "Moose K.C.", lname = "Candido")


  

main()



