# Programming Trump Vine
# Created by Prof. C

# Constant for the growth per year.
GROWTH_FACTOR = 2

# Declare a variable to store the rise.
fLength = float(input("Enter starting length: "))
iYearMax = int(input("How many years: "))

# Calculate and print value for the rise each year.
print ('Year\t\tProjected Length')
print ('------------------------------------------')

for iYear in range(1, iYearMax + 1):
    fLength *= GROWTH_FACTOR
    print (iYear, '\t\t', format(fLength, '.2f'))
