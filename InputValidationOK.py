# Sample of input a validation attempt
# Nice intentions but not the best...

# Get Test 1 score.
iTest1 = int(input("Test 1: "))

# Test to see if test 1 is valid and give an extra attempt:
if iTest1 <= 0:
    print("\nTest scores must be greater than 0!")
    iTest1 = int(input("Test 1: "))
    if iTest1 <= 0:
        print("Test scores must be greater than 0!")
        raise SystemExit
