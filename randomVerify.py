# In Class Programming Exercise
# the guessing game. 

import random

# main function
def main():

    outfile = open('randomVerify.txt', 'w')

    iNumber = 0
    # Initializing local variables
    while iNumber != 100 :
        iNumber = random.randint(1, 100)
        outfile.write(str(iNumber) + '\n')


    outfile.close()


# Call the main function.
main()


