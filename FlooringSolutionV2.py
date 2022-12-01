# Flooring calculator

nSCRAP_FACTOR = .1
nSQUARE_YARDS = 9

# 1.Input both the Length and Width:
nLength = float(input("Room Length: "))
nWidth = float(input("Room Width: "))

# 2. Calculate
# 2.1 Area is Length x Width
nArea = nLength * nWidth

# 2.2 Scrap is 10% of the calculated area:
nScrap = nArea * nSCRAP_FACTOR

# 2.2 Total
nTotal = nArea + nScrap

# 3. Output:
#    Area of the room:
#    Scrap value:
#    Total of Area + Scrap:
#    Total Square Yards which is Total / 9

print("Area of the room is:       " + format(nArea,'10.2f'))
print("Scrap for the room is:     " + format(nScrap,'10.2f'))
print("Total Area and Scrap of the room is: " + format(nTotal ,'10.2f'))
print("Total Square Yards of the room is:   " + format(nTotal / nSQUARE_YARDS,'10.2f'))

print("---------------------")
print("Another way to format")
print("---------------------")

# OR format this way by creating 2 columns: one for String Formatted and one for Number formatted:
print(format("Area of the room is:", "40s"), format(nArea,'10.2f'))
print(format("Scrap for the room is:", "40s"), format(nScrap,'10.2f'))
print(format("Total Area and Scrap of the room is:", "40s"), format(nTotal ,'10.2f'))
print(format("Total Square Yards of the room is:","40s"), format(nTotal / nSQUARE_YARDS,'10.2f'))


