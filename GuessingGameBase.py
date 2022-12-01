# In Class Programming Exercise
# the guessing game. 

import random

# main function
def main():

    # Initializing local variables
    iSecretNumber = 0
    iPlay = 1

    # Continue presenting numbers for the user
    # to guess while the user wants to continue
    # playing.
    while(iPlay > 0):
        iSecretNumber = random.randint(1, 100)
        iPlay = playGuessingGame(iSecretNumber)

    print('Thanks for playing it was fun!')

# The playGuessingGame function receives the number that the
# user has to guess as an argument and prompts the user for
# guesses. If the user guesses incorrectly he/she is notified,
# and is prompted to try again. Otherwise, the user's guess
# is returned.
#
# You must code this:
# 1. Enter a loop that will continue to loop until 1 of 2 things occurs:
#    1.1 The user types in a 0 to end the game
#    1.2 The user wins the game by guessing the randomly generated number
# 2. Prompt the user for a number between 1 and 100
# 3. Check the User Entered Number
#    3.1 If User Entered Number = 0 stop the game
#    3.2 If User Entered Number > Secret Number print out 'Too high, try again'
#    3.3 If User Entered Number < Secret Number print out 'Too low, try again'
#    3.4 If User Entered Number = Secret Number print out 'You got it!'

#--------> Put the playGuesingGame Function here:




# Call the main function.
main()


