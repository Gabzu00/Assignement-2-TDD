import random


class dice:
    
    def throwDice():
        """Generera siffra mellan 1 och 6"""
        return random.randint(1,6)

    """Visa vilken symbol som man får"""

    def diceOne():
        return"⚀ --> You got a one!"
            
    def diceTwo():
        return"⚁ --> You got a two!"

    def diceThree():
        return"⚂ --> You got a three!"

    def diceFour():
        return"⚃ --> You got a four!"

    def diceFive():
        return"⚄ --> You got a five!"

    def diceSix():
        return"⚅ --> You got a six!" 

