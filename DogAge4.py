# Fourth Dog Age Calculator
# Version 4 has Named Constants and Formatting:

#Named Constant
nHUMAN_EQUIVALENT = 7.3

#1. Input
sAge = input("Input your dogs age: ")

#2. Convert:
fAge = float(sAge)

# 3. Compute
fHumanAge = fAge * nHUMAN_EQUIVALENT

# 4. Output:

# 4.1 Convert fHumanAge to a string with no formatting:
print("The human age equivalent for your dog is: " + str(fHumanAge))
# 4.2 Convert fHumanAge to a string with formatting and column that is 10 characters with 2 decimal points:
print("The human age equivalent formatted for your dog is: " + format(fHumanAge,'10.2f'))
      
