# Author: Prof. Candido

# Assign sQuote the value of "Chris Ortega"
sQuote = str("Chris Ortega")

# Assign sQuote2 the value of "Chris Ortega"
sQuote2 = "Chris Ortega"

# Extract each character out of the string one at a time using a while:
iPosition = 0
while iPosition < len(sQuote):
     sCharacter = sQuote[iPosition]
     print(sCharacter)
     iPosition += 1

# Extract each character out of the string one at a time using a for:
for sCharacter in sQuote:
     print(sCharacter)

# Extract every other character out of the string one at a time using a for:
for iPosition in range(0, len(sQuote), 2):
     sCharacter = sQuote[iPosition]
     print(sCharacter)

# Assign my dogs full name to 4 different variables:
sFirst = "Moose"
sMiddle1 = "Kuaui"
sMiddle2 = "Comet"
sLast  = "Bassador"

# Concatenation:
sFullName = sFirst + " " + sMiddle1 + " " + sMiddle2 + " " + sLast
print(sFullName)

# Slicing also know as substring, extracting or parsing:
sSlice = sFullName[0:5]
print(sSlice)

sSlice = sFullName[:7]
print(sSlice)

sSlice = sFullName[7:]
print(sSlice)

sSlice = sFullName[0:26:2]
print(sSlice)

sSlice = sFullName[-5:]
print(sSlice)

# Using Python's string functions:
print( len(sFullName)  )

print( sFullName.isalpha() )

print( sFullName.endswith("r")  )

print( sFullName.lower() )

print( sFullName.upper() )


# The Python string strip functions
sName1 = "----Kayla----"
sName2 = " Pasquale "

print( sName1.lstrip('-') )

print( sName1.rstrip('-') )

print( sName1.rstrip('-').lstrip('-') )
print( sName1.strip('-') )

print( len(sName2.strip())  )






     
