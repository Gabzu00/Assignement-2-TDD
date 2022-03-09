"""Tester för PvE klassen."""
import unittest
from PIG import PvE

class TestPvEClass(unittest.TestCase):

    def test_class_Start(self):
        res = PvE.Start.player1Throws
        self.assertEqual(res, 0)

    # def test_init(self):
    #     res = PvE.Start.init()
    #     self.assertEqual(res, )
        
