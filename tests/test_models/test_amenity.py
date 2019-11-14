#!/usr/bin/python3
from datetime import datetime
from models.amenity import Amenity
import unittest
"""Test Amenity module"""


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up class"""
        cls.bm = Amenity()
        cls.n = datetime.now()
        cls.bm2 = Amenity()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance
