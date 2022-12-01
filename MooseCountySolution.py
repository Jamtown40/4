# work with if statements - Moose County Fair
# Prof. C


iAge = int( input("What is your age: ") )

if iAge <= 5:
    fAdmission = 0.0

if iAge >= 6 and iAge <= 12:
    fAdmission = 4.0

if iAge >= 13 and iAge <= 18:
    fAdmission = 5.0
  
if iAge >= 19 and iAge <= 22:
    fAdmission = 6.0

if iAge >= 23 and iAge <= 64:
    fAdmission = 8.5

if iAge >= 65:
    fAdmission = 6.0

print("For the age: ", iAge, "Admission is: $", format(fAdmission, ",.2f"))


# Option 2:

iAge = int( input("What is your age: ") )

if iAge <= 5:
    fAdmission = 0.0
elif iAge >= 6 and iAge <= 12:
    fAdmission = 4.0
elif iAge >= 13 and iAge <= 18:
    fAdmission = 5.0
elif iAge >= 19 and iAge <= 22:
    fAdmission = 6.0
elif iAge >= 23 and iAge <= 64:
    fAdmission = 8.5
else: 
    fAdmission = 6.0

print("For the age: ", iAge, "Admission is: $", format(fAdmission, ",.2f"))

# Option 3:

iAge = int( input("What is your age: ") )

if iAge <= 5:
    fAdmission = 0.0
elif iAge <= 12:
    fAdmission = 4.0
elif iAge <= 18:
    fAdmission = 5.0
elif iAge <= 22:
    fAdmission = 6.0
elif iAge <= 64:
    fAdmission = 8.5
else: 
    fAdmission = 6.0

print("For the age: ", iAge, "Admission is: $", format(fAdmission, ",.2f"))


