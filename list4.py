
# Set up a list with no values:
sStudentList = []
iGrades = []

# Ask the user for a name and keep looping asking for a name
# until the user types in a small q:
sName = input("Give me a student name: ")
while sName != "q":

     iGradeInput = int(input("What is " + sName + " grade: "))
     # Check tos see if the name is already in the list: 
     if sName in sStudentList:
          # If in the list let the user know the name is in the list: 
          print(sName,"is already there.")
     else:
          # Else: Add the name to the llist
          sStudentList.append(sName)
          iGrades.append(iGradeInput)

     sName = input("Give me a student name: ")

# After exiting the loop sort the list: 


# Put each name entry/element in the list out to the screen on
# its own line:
iElement = 0
while iElement < len(sStudentList):
     print(sStudentList[iElement], "got a:", iGrades[iElement])
     iElement += 1



          

