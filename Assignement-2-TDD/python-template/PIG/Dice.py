import random

def throwDice():
    """Generera siffra mellan 1 och 6"""
    return random.randint(1,6)

"""Visa vilken symbol som man får"""

def diceOne():
    return" ______\n|      |\n|   •  |\n|______|\nYou got a one!"
        
def diceTwo():
    return" ______\n|      |\n|  ••  |\n|______|\nYou got a two!"

def diceThree():
    return" ______\n|      |\n|  ••• |\n|______|\nYou got a three!"

def diceFour():
    return" ______\n|      |\n| •••• |\n|______|\nYou got a four!"

def diceFive():
    return" _______\n|       |\n| •   • |\n|   •   |\n| •   • |\n|_______|\nYou got a five!"

def diceSix():
    return" _______\n|       |\n| •   • |\n| •   • |\n| •   • |\n|_______|\nYou got a six!" 
