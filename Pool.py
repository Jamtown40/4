# Named Constants

fPI = 3.14
fGALLONS_FACTOR = 7.5

sPoolType = input("Type of pool S for Square/Rectangle or C for Circular: ")

# Get inputs for either Circular or Square: 
if sPoolType == "C":
     fDiameter = float(input("What is the Diameter of the pool in feet: "))
elif sPoolType == "S":
     fLength = float(input("What is the Length of the pool in feet: "))
     fWidth = float(input("What is the Width of the pool in feet: "))
else:
     print("Must enter a C or S")
     raise SystemExit
     

# Calculate Average Depth HERE because it is needed by both types of pools
fDepth1 = float(input("What is the Depth of the pool in the Shallow end in feet: " ))
fDepth2 = float(input("What is the Depth of the pool in the Deep end in feet: "))
fAvgDepth = (fDepth1 + fDepth2) / 2

# Calculate:
if sPoolType == "C":
     fRadius = fDiameter / 2
     fCubicFeet = fPI * (fRadius * fRadius) * fAvgDepth

     # or:
     fCubicFeet = fPI * ( (fDiameter / 2) ** 2) * fAvgDepth
else:
     fCubicFeet = fLength * fWidth * fAvgDepth

# Calculate this HERE because both Square or Cicular use the same calculation:
fGallons = fCubicFeet * fGALLONS_FACTOR
     

# Output:
print("Estimated Gallons is: ", format(fGallons, ",.2f"))
