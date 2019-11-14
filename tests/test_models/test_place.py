#!/usr/bin/python3
from datetime import datetime
from models.place import Place
import unittest
"""Test Place module"""


class TestPlace(unittest.TestCase):
    """Test Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.bm = Place()
        cls.n = datetime.now()
        cls.bm2 = Place()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance
