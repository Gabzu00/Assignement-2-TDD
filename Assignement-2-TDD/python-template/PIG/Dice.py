"""Importerar random och skapar vår dice klass."""
import random


class dice:
    """Funktionerna för dice."""

    def throwDice():
        """Generera siffra mellan 1 och 6."""
        return random.randint(1, 6)

    """Visa vilken symbol som man får."""

    def diceOne():
        """Medelande som ska visas."""
        return"⚀ --> It was a one!"

    def diceTwo():
        """Medelande som ska visas."""
        return"⚁ --> It was a two!"

    def diceThree():
        """Medelande som ska visas."""
        return"⚂ --> It was a three!"

    def diceFour():
        """Medelande som ska visas."""
        return"⚃ --> It was a four!"

    def diceFive():
        """Medelande som ska visas."""
        return"⚄ --> It was a five!"

    def diceSix():
        """Medelande som ska visas."""
        return"⚅ --> It was a six!"
