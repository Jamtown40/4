# Author:  Prof. Candido
# Purpose: Demostrates how to format output using different samples

sInput = input("Enter a measurement in feet: ")

fFeet = float(sInput)

fInches = fFeet * 12
fMeters = fFeet * .3048

# Format the Output:
# -Format the text in a fixed column of 45 positions
# -Format the fInches variable in a fixed column of 15 positions with, thousands separators 4 decimal points:
# Note: this uses string concatenation operator +

print('{:45}'.format("Inches equivalent (fully formatted):") + '{:15,.4f}'.format(fInches) )

# Format the Output:
# -Format the text in a fixed column of 45 positions
# -Format the fInches variable in a fixed column of 15 positions with 4 decimal points:

# Note: this uses , to separate the output parameters to the print function and you MUST
#       code the sep='' so prevent Python from putting an extra space between the text parameter
#       and the formatted fMeters variable.  So Prof. C strongly recommends to use the concatenation
#       operator +
print('{:45}'.format("Meters equivalent (no thousands separators):") , "{:15.4f}".format(fMeters),sep=''  )


#
