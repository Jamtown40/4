# Programming Exercise 4-9
# Slightly modified by Prof. C

# Constant for the rise per year.
RISE_PER_YEAR = 1.6

# Declare a variable to store the rise.
fRise = 0.0
fInches = 0.0

# Calculate and print value for the rise each year.
print ('Year\t\tRise(mm)\tRise (in)')
print ('------------------------------------------')


for iYear in range(25):
    iYear += 1
    fRise = iYear * RISE_PER_YEAR
    fInches = fRise * 0.039

    print ('{0:<5} {1:>10.2f} {2:>10.2f}'.format(iYear, fRise, fInches) )
   
