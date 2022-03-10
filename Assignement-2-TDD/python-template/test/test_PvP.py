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
    
    """Testa init namn och att Hello printas."""
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

    """Testar att change name ändrar till rätt namn och att end printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer11ChangeName(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["W", "1", "Gabbe", "Q"]):
            myInstance.startPlayer1()
        
        self.assertTrue("Gabbe"  == myInstance.Player1Name)
        self.assertTrue("End" in mock_stdout.getvalue())

    """Kollat att spelare 2 ändrar sitt namn och att end printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer12ChangeName(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["W", "2", "Gabbe", "Q"]):
            myInstance.startPlayer1()
        
        self.assertTrue("Gabbe"  == myInstance.Player1Name)
        self.assertTrue("End" in mock_stdout.getvalue())

    """Testar att change name ändrar till rätt namn och att end printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer21ChangeName(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["W", "1", "Gabbe", "Q"]):
            myInstance.startPlayer2()
        
        self.assertTrue("Gabbe"  == myInstance.Player1Name)
        self.assertTrue("End" in mock_stdout.getvalue())

    """Kollat att spelare 2 ändrar sitt namn och att end printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer22ChangeName(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["W", "2", "Gabbe", "Q"]):
            myInstance.startPlayer2()
        
        self.assertTrue("Gabbe"  == myInstance.Player1Name)
        self.assertTrue("End" in mock_stdout.getvalue())

    """Testar att tärningen kastas och att End printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1Throw(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["Y", "Q"]):
            myInstance.Player1Throw()
        
        self.assertTrue("End" in mock_stdout.getvalue())

    """Kollar att spelare får 100 poäng och att wins!!! printas."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1Cheat(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["C"]):
            myInstance.startPlayer1()
        
        self.assertTrue(myInstance.player1Total == 100)
        self.assertTrue("wins!!!" in mock_stdout.getvalue())
        
    """Kollar att End printas om spelare väljer att avsluta."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1End(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["N", "Q"]):
            myInstance.startPlayer1()
        
        self.assertTrue("End" in mock_stdout.getvalue())
    
    """Kollar att tärningen kastas och att End printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer2(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["P", "Y", "Q"]):
            myInstance.startPlayer2()
        
        self.assertTrue("End" in mock_stdout.getvalue())

    """Kollar att tärningen kastas och att End printas i slutet."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["P", "Y", "Q"]):
            myInstance.startPlayer1()
        
        self.assertTrue("End" in mock_stdout.getvalue())

    """Kollar att spelare får 100 poäng och att wins!!! printas."""
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer2Cheat(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["C"]):
            myInstance.startPlayer2()
        
        self.assertTrue(myInstance.player2Total == 100)
        self.assertTrue("wins!!!" in mock_stdout.getvalue())
    
    """Kollar att End printas om spelare väljer att avsluta."""   
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer2End(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["N"]):
            myInstance.startPlayer2()
        
        self.assertTrue("End" in mock_stdout.getvalue())
    
    """Testar att tärningen kastas och att End printas i slutet."""   
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer2Throw(self, mock_stdout):
        myInstance = PvP.Start
        with mock.patch('builtins.input', side_effect=["Y", "Q"]):
            myInstance.Player2Throw()
        
        self.assertTrue("End" in mock_stdout.getvalue())
    
        
        
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_Win1(self, mock_stdout):
    #     myInstance = PvP.Start
    #     with mock.patch('builtins.input', side_effect=["C"]):
    #         myInstance.startPlayer1()

    #     self.assertTrue("End" in mock_stdout.getvalue())
        
    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_Win2(self):
    #     myInstance = PvP.Start
    #     with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         myInstance.Win2()

    #     self.assertTrue("End" in fake_stdout.getvalue())
    
    # @patch('sys.stdout', new_callable=io.StringIO) 
    # def test_printValue(self):
    #     myInstance = PvP.Start
    #     with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    #         myInstance.printValue()
            
    #     self.assertTrue("" in fake_stdout.getvalue())