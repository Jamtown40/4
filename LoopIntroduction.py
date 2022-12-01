# Professor Candido

# If I want to print out 1 through 10.  Below are three options...


# Option 1: Have 10 different print statements.  This works...but...
#           what happens when I want to print out a 1 to 100 or 1 to 1000???
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# Option 2: Use a Python while loop.  Start at 1 and repeat until you exceed 10
#           not I must start at 1, end at 10 and then add 1 to iNumber. The code
#           from Option 1 is now reduced to 4 lines!!!
iNumber = 1
while iNumber <= 10 :
    print(iNumber)
    iNumber += 1

# Option 3: Use a Python for loop.  Start at 1 and stop at 11 but do NOT include 11.
#           the for will use the Python range function. The code from Option 2 is now
#           reduced to 2 lines!!!!

for iNumber in range(1,11):
    print(iNumber)


# Which do you like best: Option 1, Option 2 or Option 3???

