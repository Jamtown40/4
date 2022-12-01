# Prof. Candido
# Chapter 5 challenge to code functions


def ToInches(fFeetIn):
     return fFeetIn * 12

def ToCentimeters(fFeetIn):
     return fFeetIn * 30.48

def ToMeters(fFeetIn):
     return fFeetIn * .3048


def main():
     # 
     fFeet = float(input("Enter the number of feet (partial values are OK): "))

     print("You entered:", fFeet,"feet")

     #Way 1 using function calls:
     fInches = ToInches(fFeet)
     fCentimeters = ToCentimeters(fFeet)
     fMeters = ToMeters(fFeet)

     print("Converted to inches is:", format(fInches,".2f") )
     print("Converted to centimeters is:", format(fCentimeters,".2f") )
     print("Converted to meters is:", format(fMeters,".2f") )



     #Way 2 using function nesting:
     print("\nOutput using function nesting")
     print("You entered:", fFeet,"feet")
     
     print("Converted to inches is:", format(ToInches(fFeet),".2f")  )
     print("Converted to centimeters is:", format(ToCentimeters(fFeet),".2f") )
     print("Converted to meters is:", format(ToMeters(fFeet),".2f") )
     

# Call the main() function:   
main()
