"""Tester för PvE klassen."""
import unittest 
from unittest import mock
from PIG import Main
import io
from unittest.mock import patch

class TestPvEClass(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer1End(self, mock_stdout):
        myInstance = Main.startMain
        with mock.patch('builtins.input', side_effect=["2", "1", "Gabriel", "Q"]):
            myInstance.main()
        
        self.assertTrue("Instructions" in mock_stdout.getvalue())
        
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_startPlayer2End(self, mock_stdout):
        myInstance = Main.startMain
        with mock.patch('builtins.input', side_effect=["1", "n1", "n2", "Q"]):
            myInstance.main()
        
        self.assertTrue("End" in mock_stdout.getvalue())
