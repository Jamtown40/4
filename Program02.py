# Author Prof C
# Purpose: Work with inputting numeric values


# Input
sName = input("What is your name: ")

# TWO step process to accept input as a string
# and convert an int
sAge = input("What is your age as an int: ")
iAge = int(sAge)

# OR ONE step process to accept input as a string
# and convert an int

iAge = int(input("What is your age as an int: "))

print("Hello", sName,"You are:",iAge,"old")


# If you want to have a float input so you can have
# decimal values use the float() function:
fAge = float(input("What is your age as a float: "))
print("Hello", sName,"You are:",fAge,"old")




