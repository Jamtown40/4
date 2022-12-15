# This program will work with string and float 
# lists to experiement with data analysis.

import statistics


sStudents = ["Moose","Adam","Jon","James","Brianna","Prof C"]
fSample = [6.25,4,2.1,8.99]

print("Elements/entries:", len(sStudents) )
print("Lowest value:", min(sStudents) )
print("Lowest value:", max(sStudents)      )
print("Value 2:", sStudents[2]      )

#print("Attempt to sum:", sum(sStudents) )


print('---------------------------')    

print("Elements/entries:", len(fSample) )
print("Lowest value:", min(fSample) )
print("Lowest value:", max(fSample)      )
print("Value 2:", fSample[2]      )

print("Attempt to sum:", sum(fSample) )

print("Attempt to avg:", sum(fSample) / len(fSample) )

print("Attempt to avg:", statistics.mean(fSample)  )




            
