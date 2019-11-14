#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    """TestFileStorage - test class for file strorage file"""
    b = BaseModel()
    b.name = "lime"

    def test_file_not_none(self):
        """test"""
        with open("file.json") as f:
            self.assertIsNotNone(f.read())

    def test_file_(self)