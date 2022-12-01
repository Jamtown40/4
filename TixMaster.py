# Professor Candido

# Ticket Master




iTixMax = int(input("Enter number of total tickets: "))

for iNbr in range(1,iTixMax + 1):
    print( '+-------------------------------------+')
    print( '|        STCC Welcomes Linus          |')
    print( '|             04/04/2022              |')
    print(f'|           {iNbr:5.0f} of {iTixMax:5.0f}            |')
    print( '+-------------------------------------+')      
    print('\n\n')
    
iNbr = 1
while iNbr <= iTixMax:
    print( '+-------------------------------------+')
    print( '|        STCC Welcomes Linus          |')
    print( '|             04/04/2022              |')
    print(f'|           {iNbr:5.0f} of {iTixMax:5.0f}            |')
    print( '+-------------------------------------+')      
    print('\n\n')
    iNbr += 1




#iMaxFormatLength = str(len(str(iTixMax) ) )+ ".0f"

#   print( '|              ' + format(iNbr,"2.0f") + ' of ' + format(iTixMax,"2.0f") + '               |')
#   print(f'|              {format(iNbr,"2.0f")} of {format(iTixMax,"2.0f")}               |')
#   print(f'|              {format(iNbr,iMaxFormatLength)} of {format(iTixMax,iMaxFormatLength)}               |')      







