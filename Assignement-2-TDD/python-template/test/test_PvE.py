"""Tester för PvE klassen."""
import unittest
from PIG import PvE

class TestPvEClass(unittest.TestCase):

    def test_class_start(self):
        res = PvE.Start.player1Throws
        self.assertEqual(res, 0)
