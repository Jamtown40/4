#Author: ??
# Check out this code a student submitted and learn from it :)

# Please identify all the code:
# -That Is wrong and needs to be fixed
# -Code that is Unnecessary or inefficent:
# -Or things are just plain wrong

print ("Welcome to the BMI Analyzer")
sName = str(input ("Please input your name:")) 
sHeight = int(input ("Please input your height in inches:"))
sWeight = int(input ("Please input your weight in pounds:"))       

#Named constance
fMeter = 0.0254
fKilo = 0.45359237

#Calculations:
sMeter = float( sHeight * fMeter )
sKilo = float( sWeight * fKilo )

fBMI = (float (sKilo / ( sMeter * sMeter)))

if fBMI <= 18.50:
    sMessage = ("Underweight")
elif fBMI > 18.50 and fBMI <= 24.90:
     sMessage = ("Normal")
elif fBMI > 24.91 and fBMI <= 29.90:
     sMessage = ("Overweight")
elif fBMI > 29.90:
     sMessage = ("Obese")
    
print("Your BMI is:",format(fBMI, "0.2f"))
print(sName, "is found to be:",(sMessage))
