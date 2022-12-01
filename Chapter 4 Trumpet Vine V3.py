# Programming Trump Vine
# Created by Prof. C

# Constant for the growth per year.
GROWTH_FACTOR = 2

# While code:
print ("\nWhile Code:")

# Prompt for input for initial length and years:
fLength = float(input("Enter starting length: "))
iYearMax = int(input("How many years: "))
       
print ( '{0:<5}{1:>16}{2:>16}'.format("Year", "Projected Length", "Inches") )

# Calculate and print value for the growth each year.

iYear = 1
while iYear <= iYearMax :
    fLength *= GROWTH_FACTOR
    print ( '{0:<5}{1:>16.2f}{2:>16.2f}'.format(iYear, fLength, fLength * 12) )
    iYear += 1
