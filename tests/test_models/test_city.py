#!/usr/bin/python3
from datetime import datetime
from models.city import City
import unittest
"""Test City module"""


class TestCity(unittest.TestCase):
    """Test State class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.bm = City()
        cls.n = datetime.now()
        cls.bm2 = City()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance
