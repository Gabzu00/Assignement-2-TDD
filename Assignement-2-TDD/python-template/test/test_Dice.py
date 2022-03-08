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
        self.assertTrue(exp == "⚀ --> It was a one!") 
        
    def test_diceTwo(self):
        res = Dice.dice
        exp = res.diceTwo()
        self.assertTrue(exp == "⚁ --> It was a two!")
        
    def test_diceThree(self):
        res = Dice.dice
        exp = res.diceThree()
        self.assertTrue(exp == "⚂ --> It was a three!")    
        
    def test_diceFour(self):
        res = Dice.dice
        exp = res.diceFour()
        self.assertTrue(exp == "⚃ --> It was a four!")
        
    def test_diceFive(self):
        res = Dice.dice
        exp = res.diceFive()
        self.assertTrue(exp == "⚄ --> It was a five!")
        
    def test_diceSix(self):
        res = Dice.dice
        exp = res.diceSix()
        self.assertTrue(exp == "⚅ --> It was a six!")
        
    def test_one(self):
        res = Dice.dice
        exp = res.diceOne()
        self.assertFalse(exp == "⚀")
        
    def test_two(self):
        res = Dice.dice
        exp = res.diceTwo()
        self.assertFalse(exp == "⚁")
        
    def test_three(self):
        res = Dice.dice
        exp = res.diceThree()
        self.assertFalse(exp == "⚂")
        
    def test_four(self):
        res = Dice.dice
        exp = res.diceFour()
        self.assertNotEqual(exp, "⚃")
        
    def test_five(self):
        res = Dice.dice
        exp = res.diceFive()
        self.assertNotEqual(exp, "⚄")
        
    def test_six(self):
        res = Dice.dice
        exp = res.diceSix()
        self.assertNotEqual(exp, "⚅")
        
    def test_throw_dice1(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertLess(exp, 7)
        
    def test_throw_dice2(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertLess(exp, 8)
        
    def test_throw_dice3(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertLess(exp, 9)
        
    def test_throw_dice4(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertGreater(exp, 0)
    
    def test_throw_dice5(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertLess(exp, 10)
        
    def test_throw_dice6(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertLess(exp, 11)
        
    def test_throw_dice7(self):
        res = Dice.dice
        exp = res.throwDice()
        self.assertLess(exp, 12)