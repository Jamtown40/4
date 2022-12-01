
# Set up a list with no values:
sStudentList = []

# Ask the user for a name and keep looping asking for a name
# until the user types in a small q:
sName = input("Give me a student name: ")
while sName != "q":

     # Check tos see if the name is already in the list: 
     if sName in sStudentList:
          # If in the list let the user know the name is in the list: 
          print(sName,"is already there and Victor sayz you are dumb")
     else:
          # Else: Add the name to the llist
          sStudentList.append(sName)

     sName = input("Give me a student name ")

# After exiting the loop sort the list: 
sStudentList.sort()

# Put each name entry/element in the list out to the screen on
# its own line:
for sName in sStudentList:
     print(sName)



          

