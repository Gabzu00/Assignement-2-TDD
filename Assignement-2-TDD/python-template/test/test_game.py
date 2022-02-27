#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from PIG import Game


class TestGameClass(unittest.TestCase):
    """Test the class."""

    """"def test_init_default_object(self):
        res = Game()
        self.assertIsInstance(res)""" ""

    def test_HelloWorld(self):
        res = Game.HelloWorld()
        self.assertEqual(res, "Hello World")


if __name__ == "__main__":
    unittest.main()
