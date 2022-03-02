#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from PIG import Main


class TestMainClass(unittest.TestCase):
    """Test the class."""

    def test_HelloWorld(self):
        res = Main.HelloWorld()
        self.assertEqual(res, "Hello World")


if __name__ == "__main__":
    unittest.main()
