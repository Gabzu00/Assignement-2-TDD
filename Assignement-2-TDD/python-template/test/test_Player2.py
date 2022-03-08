"""Tester för Player2 classen."""
import unittest
from PIG import Player2


class TestPlayer2Class(unittest.TestCase):

    def test_constructor(self):
        """Testa om funktionen skapar ett objekt."""
        res = Player2.Player_class("Test", 0)
        self.assertIsInstance(res, object)
    
    def test_throw_score(self):
        """Testa om man kan ändra spelarens poäng."""
        res = Player2.Player_class("Test", 0)
        res.ThrowScore(1)
        exp = 1
        self.assertTrue(exp == res.score)

    def test_change_name(self):
        """Testa om man kan ändra namn på spelaren."""
        res = Player2.Player_class("Test", 0)
        res.changeName("test_change")
        exp = "test_change"
        self.assertTrue(exp == res.name)
