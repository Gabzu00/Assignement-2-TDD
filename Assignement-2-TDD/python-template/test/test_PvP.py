"""Tester för PvE klassen."""
import unittest 
from unittest import mock
from PIG import PvP
import io
from unittest.mock import patch

class TestPvPClass(unittest.TestCase):
    
    def test_class_start(self):
        res = PvP.Start
        exp = res.player1Score
        self.assertEqual(exp, 0)
        
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_init(self, mock_stdout):
        myInstance = PvP.Start

        player1name = "N1"
        player2name = "N2"
        with mock.patch('builtins.input', side_effect=[player1name, player2name]):
            myInstance.init()
        
        self.assertTrue(player1name  == myInstance.Player1Name)
        self.assertTrue(player2name  == myInstance.Player2Name)
        self.assertTrue("Hello" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1ChangeName(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["W", "1", "Gabbe", "Q"]):
            myInstance.startPlayer1()
        
        self.assertTrue("Gabbe"  == myInstance.Player1Name)
        self.assertTrue("End" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1Throw(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["Y", "Q"]):
            myInstance.startPlayer1()
        
        self.assertTrue("End" in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1Cheat(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["C"]):
            myInstance.startPlayer1()
        
        self.assertTrue(myInstance.player1Total == 100)
        self.assertTrue("wins!!!" in mock_stdout.getvalue())
