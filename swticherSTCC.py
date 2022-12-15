def getStateTax(sState):
    fOutput = 0.0

    if sState == "MA":
        fOutput = .0625
    elif sState == "CT" or sState == "NC":
        fOutput = .06
    elif sState == "ME":
        fOutput = .085
    elif sState == "NH":
        fOutput = .0
    elif sState == "RI":
        fOutput = .07
    elif sState =="VT":
        fOutput = .06
    elif sState =="TX":
        fOutput = .025
    elif sState =="CA":
        fOutput = .098
    elif sState =="SD":
        fOutput = .045
    elif sState =="TN":
        fOutput = .045
    else:
        fOutput = .0

    return fOutput


def main():

    sStateInputted = input("Enter a state abbreviation: ")
    print( getStateTax(sStateInputted ) )
    print( getSalesTax2(sStateInputted ) )
    

main()
