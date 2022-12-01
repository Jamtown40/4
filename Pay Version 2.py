#1. Constants

fOVER_TIME_HOURS = 40.0
fDOUBLE_TIME_HOURS = 60.0

# 2. Get input:
fHours = float( input("Enter hours worked: ") )
fPayRate = float( input("Enter hourly rate: ") )

fDoubleTimeHours = 0.0
fHalfTimeHours = 0.0


# 2. Determine Over Time and Double Time:

# 2.1 Check if worked more than 40 hours:
if fHours > fOVER_TIME_HOURS :

   # 2.2 Check if any double time hours:  
   if fHours > fDOUBLE_TIME_HOURS:
        fDoubleTimeHours = fHours - fDOUBLE_TIME_HOURS
        fHours = fHours - fDoubleTimeHours
        
   # 2.3 Determine time and half hours:
   fHalfTimeHours = fHours - fOVER_TIME_HOURS
   fHours -= fHalfTimeHours
   

# 3. Calculate pay:
fRegularPay    = fHours * fPayRate
fHalfTimePay   = fHalfTimeHours * (fPayRate * 1.5) 
fDoubleTimePay = fDoubleTimeHours * (fPayRate * 2) 

fTotalPay = fRegularPay + fHalfTimePay + fDoubleTimePay

# 4. Output:

print("Regular Pay is: $ ", format( fRegularPay ,',.2f'))
print("Time and Half Pay is: $ ", format( fHalfTimePay ,',.2f'))
print("Double Time Pay is: $ ", format( fDoubleTimePay ,',.2f'))
print("Total Pay is: $ ", format( fTotalPay ,',.2f'))
