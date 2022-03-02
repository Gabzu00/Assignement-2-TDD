import unittest
import random
from PIG import Dice


class TestDiceClass(unittest.TestCase):
    
    def test_throwDice(self):
        """Testa classen"""
        res = Dice.throwDice()
        exp = random.randint(1,6)
        
        self.assertEqual(res, exp)
        
        
if __name__ == "__main__":
    unittest.main()