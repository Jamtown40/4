# Sample of outputting strings and floats with columns
sName = input("Give me a name: ")
fSalary = float(input("Give me a salary: "))

sName2 = input("Give me a second name: ")
fSalary2 = float(input("Give me a second salary: "))

sName3 = input("Give me a second name: ")
fSalary3 = float(input("Give me a second salary: "))


# '{:20}' means to get a left justfield column that is 20 characters wide
#         so my name Brian would take up 5 characters and then I get 15 blanks

# "15,.2f" means to get a right justfield column that is 15 characters wide
#          with comma thousands separators and a decimal point and 2 decimal
#          positions so 45325.257 would display as 45,325.26

print( '{:20}'.format(sName),  format(fSalary, "15,.2f") )

# Second output to show how the columns line up:
print( '{:20}'.format(sName2), format(fSalary2, "15,.2f") )

# You can use another approach:

# Third output to show how the columns line up:
print( format(sName3,"20s"), format(fSalary3, "15,.2f") )
