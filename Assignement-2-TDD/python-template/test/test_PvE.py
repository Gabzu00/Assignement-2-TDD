<<<<<<< HEAD

=======
"""Tester för PvE klassen."""
import unittest
from PIG import PvE
import io
import sys
import os


class TestPvEClass(unittest.TestCase):

    def test_class_Start(self):
        res = PvE.Start.player1Throws
        self.assertEqual(res, 0)

<<<<<<< HEAD
    def test_init(self):
        res = PvE.Start.init()
        exp = PvE.Start.init()
        self.assertEqual(exp, res)

    #def test_startPlayer(self):
    #    capturedOutput = sys.stdout
    #    sys.stdout = io.StringIO()
    #    res = PvE.Start
    #    res.startPlayer()
    #    sys.stdout = sys.__stdout__
    #    exp = res.difficulty

    #    self.assertTrue(res == 0)
=======
    # def test_init(self):
    #     res = PvE.Start.init()
    #     self.assertEqual(res, )
>>>>>>> 1c0d41f72835f8fc5dcb7c6f2bfde73593925701
        
>>>>>>> 47cb1a2f99e38546b55cbdd28477e217c1874efb
