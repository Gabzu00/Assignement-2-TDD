"""Tester för PvE klassen."""
import unittest 
from unittest import mock
from PIG import PvE
import io
from unittest.mock import patch


class TestPvEClass(unittest.TestCase):

    def test_class_start(self):
        res = PvE.Start
        exp = res.player1Score
        self.assertEqual(exp, 0)
        
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_init(self, mock_stdout):
        myInstance = PvE.Start
        playerName = "Gabriel"
        with mock.patch('builtins.input', side_effect=["2" ,playerName]):
            myInstance.init()

        self.assertTrue(playerName  == myInstance.PlayerName)
        self.assertTrue("Hello" in mock_stdout.getvalue())
     
    """Testar om det går att byta namn och om temporary printas."""   
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayerChangeName(self, mock_stdout):
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["W", "Gabbe", "Q"]):
            myInstance.startPlayer()
        
        self.assertTrue("Gabbe"  == myInstance.PlayerName)
        self.assertTrue("Temporary" in mock_stdout.getvalue())

    """Testar att tärningen kastas och att End printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayerThrow(self, mock_stdout):
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["Y", "Q"]):
            myInstance.PlayerThrow()
            
        self.assertTrue("dice!" in mock_stdout.getvalue())
        self.assertTrue("End" in mock_stdout.getvalue())
        
    """Kollar att spelare får 100 poäng och att win!!! printas."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayerCheat(self, mock_stdout):
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["C"]):
            myInstance.startPlayer()
        
        self.assertTrue(myInstance.player1Total == 100)
        self.assertTrue("win!!!" in mock_stdout.getvalue())
        
    # """Kollar att End printas om spelare väljer att avsluta."""
    # @patch('sys.stdout', new_callable=io.StringIO) 
    # def test_startPlayer1End(self, mock_stdout):
    #     myInstance = PvE.Start
    #     with mock.patch('builtins.input', side_effect=["N", "Q"]):
    #         myInstance.startPlayer()
        
    #     self.assertTrue("play" in mock_stdout.getvalue())
        
    # @patch('sys.stdout', new_callable=io.StringIO) 
    # def test_startThrowDifficultBot(self, mock_stdout):
    #     myInstance = PvE.Start
    #     with mock.patch('builtins.input', side_effect=["1", "Player1"]):
    #         myInstance.init()
    #     with mock.patch('builtins.input', side_effect=["N", "Q"]):
    #         myInstance.option(1)

    #     self.assertTrue("End" in mock_stdout.getvalue())


