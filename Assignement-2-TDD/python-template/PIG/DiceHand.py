"""Vad spelaren har i handen och vad som händer därefter"""

import Dice

class Start():
    def Throw():
        """Instanciera ett object från Dice klassen"""
        die = Dice.dice
        
        """Använd objectet för att kastat tärningen och printa värdet"""
        roll = die.throwDice()
        print("You rolled the dice!")
        print(f"It was a {roll}")
        
    