
#input variables
iTemp = int(input("What is the temp outside? "))

sMessage = "Cold" if iTemp <= 40 else "Chilly" if iTemp <= 60 else "Warm" if iTemp < 75 else "Hot"

print(iTemp,"is considered:", sMessage)


   
