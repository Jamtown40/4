# Sample of input a validation attempt
# Best Approach

# Get Test 1 score.
iTest1 = 0
# Keep asking until the user types in a number 0 or greater
while iTest1 <= 0 :
    
 # Attempt to convert user input to an integer
 try :   
    iTest1 = int(input("Test 1: "))
    # If there is a problem converting to an integer
    # monitor for the ValueError exception and inform
    # the user: 
 except ValueError:
    print("Input must a numeric value")

