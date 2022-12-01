import random

def getRandomNumber(iLow, iHigh):
    return random.randint(iLow, iHigh)
    

def main():

    #1. Welcome Message:
    print(" ---")
    print("( 8 ) Professor C's Magic 8 Ball Game")
    print(" ---")


    #2 Make a list:
    lstRespones = [
                    "As I see it, yes.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don’t count on it.",
                    "It is certain.",
                    "It is decidedly so.",
                    "Most likely.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Outlook good.",
                    "Reply hazy, try again.",
                    "Signs point to yes.",
                    "Very doubtful.",
                    "Without a doubt.",
                    "Yes.",
                    "Yes – definitely.",
                    "You may rely on it.",
                    "Hell No!"
                  ]
    
    #3. Ask question:
    while True:
        sQuestion = input("What is your question (enter to quit)? ")
        if sQuestion == "":
            break
        # 3.1 Get Random number:
        iEntry = getRandomNumber(0, len(lstRespones) - 1  )
        print(   lstRespones[iEntry],"\n"   )
        
        


main()






 
