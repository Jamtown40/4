sWord = input("Enter a word that will be checked to be a palindrome: ")
sWordReversed=""

for iIndex in range( len(sWord) -1 , -1, -1 ):
    print( sWord[iIndex] )
    sWordReversed += sWord[iIndex]

print(sWord, sWordReversed)

if sWord.lower() == sWordReversed.lower() :
    print("Is a palindrome")
else:
    print("Is NOT a palindrome")



print("Way 2--------------------------------------------------------")

#Convert sWord to a list to use the reverse() function:
sWord2 = [sWord]
sWord2.reverse()
#Convert List to a String: 
sWord3 = ' '.join([ str(sCharacter) for sCharacter in sWord2])

print(sWord, sWord2, sWord3)

if sWord.lower() == sWord3.lower() :
    print("Way 2: Is a palindrome")
else:
    print("Way 2: Is NOT a palindrome")


print("Way 3--------------------------------------------------------")


# Written by Tim R. 
#Python Slice takes up to 3 parameters:
#  start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
#  stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
#  step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided.


if sWord.lower() == sWord[ : :-1].lower() :    
  print("Way 3: Is a palindrome")
else:
    print("Way 3: Is NOT a palindrome")        

   
print("Way 4--------------------------------------------------------")

# Written by Tim R. 
sWord1 = input("Enter a word: ").lower()
print("Palindrome") if sWord1[::-1] == sWord1 else print("Not a palindrome")

# Enhanced Tim R. code by from Prof. C.
print(  "Palindrome" if sWord1[::-1] == sWord1 else "Not a palindrome" ) 


##if sWord1[::-1] == sWord1:
##    print("Palindrome")
##else:
##    print("Not a palindrome")





