import unittest
from PIG import Dice


class TestDiceClass(unittest.TestCase):
    
    def test_throwDice(self):
        """Testa om funktionen genererar siffra mella 1 och 6"""
        res = Dice.dice
        exp = res.throwDice()
        self.assertTrue(0 < exp < 7)
        
    """Testar om rätt symbol printas ut"""  
    def test_diceOne(self):
        res = Dice.dice
        exp = res.diceOne()
        self.assertTrue(exp == "[1] --> It was a one!")

    def test_diceTwo(self):
        res = Dice.dice
        exp = res.diceTwo()
        self.assertTrue(exp == "[2] --> It was a two!")
        
    def test_diceThree(self):
        res = Dice.dice
        exp = res.diceThree()
        self.assertTrue(exp == "[3] --> It was a three!")
        
    def test_diceFour(self):
        res = Dice.dice
        exp = res.diceFour()
        self.assertTrue(exp == "[4] --> It was a four!")
        
    def test_diceFive(self):
        res = Dice.dice
        exp = res.diceFive()
        self.assertTrue(exp == "[5] --> It was a five!")
        
    def test_diceSix(self):
        res = Dice.dice
        exp = res.diceSix()
        self.assertTrue(exp == "[6] --> It was a six!")
