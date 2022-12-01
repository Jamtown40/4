def main():

     # Set up a list with no values:
     iStudentGradeList = [89,75,65,15,100]

     # Sort the list from A-Z
     iStudentGradeList.sort()
     # Revese the contents of the list in reverse to
     # a decending list Z-A
     iStudentGradeList.reverse()

     # Either way works to find the lowest:

     # This code will pass the entire list to the
     # Python max function to get the highest value:
     iMax = max(iStudentGradeList)

     # This code will take the first entry which should
     # be the highest due to the reverse sort:
     iMax = iStudentGradeList[0]


     # Either way works to find the lowest:

     # This code will pass the entire list to the
     # Python min function to get the lowest value:
     iMin = min(iStudentGradeList)

     # This code will take the lsdy entry which should
     # be the lowest due to the reverse sort.  Don't forget
     # the lists are 0 based so you must subtract 1 from the
     # len function to get the last element:
     iMin = iStudentGradeList[ len(iStudentGradeList) - 1 ]

     # Another approach to find the last entry is to you
     # -1 to get the last entry in the list: 
     iMin = iStudentGradeList[ -1 ]

     # Print the entire list to the screen in 1 line:
     print(iStudentGradeList)
    
     # This code will pass the entire list to the
     # Python sum function to get the sum of all values:
     iSum = sum(iStudentGradeList)

     # Computer the avereage:
     fAvg = iSum / len(iStudentGradeList)

     print("Max:", iMax)
     print("Min:", iMin)
     print("Sum:", iSum)
     print("Avg:", fAvg)
     
# Call the main() function:
main()



