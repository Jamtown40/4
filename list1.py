
numbers = [7,12,6,8,15,21,99,100,-5]

sPetsTuple = ("Dog","Cat","Parrot","Fire Breathing Dragon","Fish","Turtle")

# Print out the entire list or tuple:
print(numbers)

print(sPetsTuple)


# Print out each individual entry in lists using for:
for element in numbers:
     print(element)

# Print out each individual entry in lists using while:
index = 0
while index < len(numbers):
     print(numbers[index])
     index +=1

# Changing each entry in list using a while loop.
# Could I have used a for loop?????
index = 0
while index < len(numbers):
     numbers[index] = numbers[index] * 2
     numbers[index] *= 2
     index +=1

print(numbers)

# Set up a list with 5 entries: 1 3 5 7 9
numbers2 = list(range(1,10, 2))
print(numbers2)

# Set up a list with 10 staring with 1 and ending with 10
numbers3 = list(range(1,11))
print(numbers3)

# set up a list with 12 entries each set 0
numbers4 = [0] * 12
print(numbers4)

# set up a list with 20 entries filled with 1, 2
numbers5 = [1,2] * 10
print(numbers5)
print( len(numbers5) )

# set up a list with string male names
boy_siblings = ['Brad', 'Michael', 'Mathias', 'Brian']
# set up a list with string female names
girl_siblings = ['Lauren', 'Karen', 'Liza' ]
# Concatenate lists:
all_siblings = boy_siblings + girl_siblings

print(all_siblings)
print( all_siblings[3] )

# set up a list with no values:
assad_family = []
#Add elements:
assad_family.append("Assad")
assad_family.append("Hifzah")
assad_family.append("Fahad")
assad_family.append("Saif")
assad_family.append("Amina")
assad_family.append("Briyan")
print(assad_family)
















