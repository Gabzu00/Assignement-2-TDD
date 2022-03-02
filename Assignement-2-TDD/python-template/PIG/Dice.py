import random





def throwDice():
    """Generera siffra mellan 1 och 6"""
    return random.randint(1,6)

def diceOne():
    """Visa vilken symbol som man får"""
    print (" ______")
    print ("|      |")
    print ("|   •  |")
    print ("|______|")
    print ("You got a one!")
        
def diceTwo():
    print (" ______")
    print ("|      |")
    print ("|  ••  |")
    print ("|______|")
    print ("You got a two!")


