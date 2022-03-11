"""Tester för PvE klassen."""
import unittest
from unittest import mock
from PIG import PvE
import io
from unittest.mock import patch


class TestPvEClass(unittest.TestCase):
    """Tester för PvE klassen."""

    """Testar att spelarens poäng är 0."""
    def test_class_start(self):
        """Testar classen Start."""
        res = PvE.Start
        exp = res.player1Score
        self.assertEqual(exp, 0)

    """Tester att namnet vi sätter går igenom och att Hello printas."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_init(self, mock_stdout):
        myInstance = PvE.Start
        playerName = "Gabriel"
        with mock.patch('builtins.input', side_effect=["0", "2", playerName]):
            myInstance.init()

        self.assertTrue(playerName == myInstance.PlayerName)
        self.assertTrue("Hello" in mock_stdout.getvalue())

    """Testar om det går att byta namn, om man kan skriva fel input och om temporary printas."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_startPlayerChangeName(self, mock_stdout):
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["X", "W", "Gabbe", "Q"]):
            myInstance.startPlayer()

        self.assertTrue("Gabbe" == myInstance.PlayerName)
        self.assertTrue("Temporary" in mock_stdout.getvalue())

    """Testar att tärningen kastas och att dice! printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_startPlayerThrow(self, mock_stdout):
        
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["Y", "Q"]):
            myInstance.PlayerThrow()

        self.assertTrue("dice!" in mock_stdout.getvalue())

    """Kollar att spelare får 100 poäng och att win!!! printas."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_startPlayerCheat(self, mock_stdout):
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["C"]):
            myInstance.startPlayer()

        self.assertTrue(myInstance.player1Total == 100)
        self.assertTrue("win!!!" in mock_stdout.getvalue())

    """Kollar att End printas om spelare väljer att avsluta."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_startPlayer1End(self, mock_stdout):
        myInstance = PvE.Start
        myInstance.waitTime = 0
        with mock.patch('builtins.input', side_effect=["N", "Q"]):
            myInstance.startPlayer()

        self.assertTrue("End" in mock_stdout.getvalue())

    """Tester om BOTen kastar och om play printas i option metoden."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_startThrowDifficultBot(self, mock_stdout):
        myInstance = PvE.Start
        with mock.patch('builtins.input', side_effect=["1", "Player1"]):
            myInstance.init()
        with mock.patch('builtins.input', side_effect=["N", "Q"]):
            myInstance.option()

        self.assertTrue("play" in mock_stdout.getvalue())

    """Testar om printvalue printar rätt meddelande."""   
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printValue2(self, mock_stdout):
        myInstance = PvE.Start
        myInstance.roll = 1
        with mock.patch('builtins.input', side_effect=["1", "Player1", "Y"]):
            myInstance.printValue(myInstance.roll)

        self.assertTrue("[1]" in mock_stdout.getvalue())

    """Testar om win printas om spelaren vinner."""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ifPlayerWin(self, mock_stdout):
        myInstance = PvE.Start
        myInstance.player1Total = 100
        with mock.patch('builtins.input', side_effect=["Y", "Q"]):
            myInstance.startPlayer()

        self.assertTrue("win" in mock_stdout.getvalue())
