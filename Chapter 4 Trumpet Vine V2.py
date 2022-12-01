# Programming Trump Vine
# Created by Prof. C

GROWTH_FACTOR = 2

# While code:
print ("\nWhile Code:")

# Prompt for input for initial length and years:
fLength = float(input("Enter starting length: "))
iYearMax = int(input("How many years: "))


print ( '{0:<5}{1:>15}'.format("Year", "Projected Length") )

# Calculate and print value for the growth each year.

iYear = 1
while iYear <= iYearMax :
    fLength *= GROWTH_FACTOR
    print ( '{0:<5}{1:>15.2f}'.format(iYear, fLength) )
    iYear += 1
