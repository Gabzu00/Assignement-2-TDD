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
        return"[1] --> It was a one!"

    def diceTwo():
        """Medelande som ska visas."""
        return"[2] --> It was a two!"

    def diceThree():
        """Medelande som ska visas."""
        return"[3] --> It was a three!"

    def diceFour():
        """Medelande som ska visas."""
        return"[4] --> It was a four!"

    def diceFive():
        """Medelande som ska visas."""
        return"[5] --> It was a five!"

    def diceSix():
        """Medelande som ska visas."""
        return"[6] --> It was a six!"
