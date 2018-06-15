import math

def FindPrimeID():

    print("Minion ID Generator")
    userInput = input("Enter any number: ")
    print("You entered: " + userInput)
    inputAsNumber = int(userInput)

    #def convertStr(s):
    #    """Convert string to either int."""
    #    try:
    #        ret = int(s)
    #    except ValueError:
    #        return ret

    def findPrimeString():
        count = 2
        primeString = ""

        while True:
            isprime = True

            for x in range (2, int(math.sqrt(count) + 1)):
                if count % x == 0:
                    isprime = False
                    break

            if isprime:
                #print(count)
                primeString += str(count)

            count += 1

            if count == 1994:
                generateId(primeString)
                break

    def generateId(primeString):
        stringId = ""
        stringId = primeString[inputAsNumber: inputAsNumber + 5]
        print(stringId)

    primeString = findPrimeString()
   
FindPrimeID() 
