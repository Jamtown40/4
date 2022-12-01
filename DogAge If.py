# Dog Age Calculator with If Logic...

# When we first wrote the Dog Age Calculator it was to gain
# practice using Python's functions: input(), int(), float()
# format() and arithmetic operators.

# Now we will enhance the initial Dog Age to include more accurate
# Calculations:
# 1. The first year of a dog's age is actually equal to 12 human years
# 2. Every years after the first year is 7.3 years.

# For example:
# A dog that is .5 (6 months old) would be 6 = .5 x 12

# A dog that is 13.75 would be 105.075 = (13.75 - 1) * 7.3 + 12



nDOG_FIRST_YEAR  = 12
nDOG_OTHER_FIRST = 7.3

# 1. Ask for dog's age.  
fAge = float( input("Input your dog's age: ") )

# 2. 1 If the dog is 1 or less use only the first year factor of 12: 
if fAge <= 1:
   fHumanAge = fAge * nDOG_FIRST_YEAR
# 2.2 Else: the dog's age is greater than 1 year so the first year of the
#     dogs age is equal to 12 months and every year after the first year
#     equates to 7.3 years:
else:
   fHumanAge = (fAge - 1) * nDOG_OTHER_FIRST + nDOG_FIRST_YEAR

# 3. Output:
print("The human age equivalent formatted for your dog is: " + format(fHumanAge,'.1f'))

