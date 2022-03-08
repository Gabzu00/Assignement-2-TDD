import unittest
from PIG import Main

class TestMainClass(unittest.TestCase):
    
    def test_main(self):
        res = Main.startMain
        exp = res.main()
        self.assertTrue(exp == "Pvp --> press '1'")
