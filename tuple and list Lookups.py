# Shows how to use a value in one table to "look up" a value in
# another table:

def main():

    # Tuple for Regions:
    tupRegions = ("East", "North", "South", "West")
    # List for Sales:
    lstSales = [50000, 45000, 75000, 90000]
    
    #Find out which Region you wish to see:
    sRegion = input("Which region do you want for sales for (East, North, South, West):")

    iPosition = tupRegions.index(sRegion)
    fSales = lstSales[iPosition]

    print("Sales for region: " + sRegion + " are: $" + '{:12,.2f}'.format(fSales))
    
# Call the main function.
main()
