import random

class dice:
    
    def throwDice():
        """Generera siffra mellan 1 och 6"""
        return random.randint(1,6)

    """Visa vilken symbol som man får"""

    def diceOne():
        return"⚀ --> It was a one!"
            
    def diceTwo():
        return"⚁ --> It was a two!"

    def diceThree():
        return"⚂ --> It was a three!"

    def diceFour():
        return"⚃ --> It was a four!"

    def diceFive():
        return"⚄ --> It was a five!"

    def diceSix():
        return"⚅ --> It was a six!" 

