"""Tester för HighScore klassen"""
import os
import unittest
from PIG import HighScore
from PIG import Player1


class TestHighScoreClass(unittest.TestCase):
    
    def test_toFile(self):
        """Testar om metoden toFile öppnar och skriver till Highscore text filen."""
        res = Player1.Player_class("Test", 0)
        HighscoreTest = HighScore.checkHighScore
        HighscoreTest.toFile(res)
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt', 'w') as add:
            check = add.closed
        exp = check
        self.assertTrue(exp == False)

    def test_read(self):
        """Testar om metoden read läser från Highscore text filen."""
        res = Player1.Player_class("Test", 0)
        HighscoreTest = HighScore.checkHighScore
        HighscoreTest.toFile(res)
        HighscoreTest.read()
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt', 'w') as add:
            check = add.closed
        exp = check
        self.assertTrue(exp == False)

    def test_addHighscore(self):
        """Testar om metoden read läser från Highscore text filen."""
        res = Player1.Player_class("Test", 0)
        HighscoreTest = HighScore.checkHighScore
        HighscoreTest.addHighScore(res.score, res)
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt', 'w') as add:
            check = add.closed
        exp = check
        self.assertTrue(exp == False)