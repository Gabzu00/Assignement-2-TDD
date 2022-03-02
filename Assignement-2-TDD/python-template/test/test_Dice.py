import unittest
from PIG import Dice


class TestDiceClass(unittest.TestCase):
    
    def test_throwDice(self):
        """Testa om funktionen genererar siffra mella 1 och 6"""
        res = Dice.throwDice()
        self.assertTrue(0 < res < 7)
      
    def test_diceOne(self):
        res = Dice.diceOne()
        self.assertTrue(res == " ______\n|      |\n|   •  |\n|______|\nYou got a one!")  
        
    def test_diceTwo(self):
        res = Dice.diceTwo()
        self.assertTrue(res == " ______\n|      |\n|  ••  |\n|______|\nYou got a two!")
        
    def test_diceThree(self):
        res = Dice.diceThree()
        self.assertTrue(res == " ______\n|      |\n|  ••• |\n|______|\nYou got a three!")    
        
    def test_diceFour(self):
        res = Dice.diceFour()
        self.assertTrue(res == " ______\n|      |\n| •••• |\n|______|\nYou got a four!")
        
    def test_diceFive(self):
        res = Dice.diceFive()
        self.assertTrue(res == " _______\n|       |\n| •   • |\n|   •   |\n| •   • |\n|_______|\nYou got a five!")
        
    def test_diceSix(self):
        res = Dice.diceSix()
        self.assertTrue(res == " _______\n|       |\n| •   • |\n| •   • |\n| •   • |\n|_______|\nYou got a six!")
        
if __name__ == "__main__":
    unittest.main()