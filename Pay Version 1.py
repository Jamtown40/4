#1. Constants

fOVER_TIME_HOURS = 40.0
fDOUBLE_TIME_HOURS = 60.0

# 2. Get input:

fHours = float( input("Enter hours worked: ") )
fPayRate = float( input("Enter hourly rate: ") )

fHalfTimePay = 0.0
fDoubleTimePay = 0.0


# 3 Calculate:

# 3.1 Check for <= 40 hours:
if fHours <= fOVER_TIME_HOURS :
   fRegularPay    = fHours * fPayRate
# 3.2 Check for <= 60 hours:   
elif fHours <= fDOUBLE_TIME_HOURS :
   fRegularPay  = fOVER_TIME_HOURS * fPayRate
   fHalfTimePay = (fHours - fOVER_TIME_HOURS )* (fPayRate * 1.5)
else:
# 3.3 Check for >= 60 hours:   
   fRegularPay    = fOVER_TIME_HOURS * fPayRate
   fHalfTimePay   = (fDOUBLE_TIME_HOURS - fOVER_TIME_HOURS )* (fPayRate * 1.5)
   fDoubleTimePay = (fHours - fDOUBLE_TIME_HOURS )* (fPayRate * 2.0)
       
# 3.4 Total Pay:
fTotalPay = fRegularPay + fHalfTimePay + fDoubleTimePay

# 4. Output:

print("Regular Pay is: $ ", format( fRegularPay ,',.2f'))
print("Time and Half Pay is: $ ", format( fHalfTimePay ,',.2f'))
print("Double Time Pay is: $ ", format( fDoubleTimePay ,',.2f'))
print("Total Pay is: $ ", format( fTotalPay ,',.2f'))
