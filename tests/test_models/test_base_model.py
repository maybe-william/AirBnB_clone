#!/usr/bin/python3
from datetime import datetime
from models.base_model import BaseModel
import unittest
"""Test base model module"""


class TestBaseModel(unittest.TestCase):
    """Test base model class"""

    @classmethod
    def setUpClass(cls):
        cls.bm = BaseModel()
        cls.n = datetime.now()
        cls.bm2 = BaseModel()
        cls.n2 = datetime.now()
        cls.ae = cls.assertEqual
        cls.ane = cls.assertNotEqual
        cls.ai = cls.assertIn
        cls.ani = cls.assertNotIn
        cls.aii = cls.assertIsInstance
        cls.anii = cls.assertNotIsInstance

    def test_id(s):
        s.ane(s.bm.id, s.bm2.id)
        s.aii(s.bm.id, str)
        s.aii(s.bm2.id, str)

    def test_created_at(s):
        s.aii(s.bm.created_at, type(s.n))

        s.ae(s.bm.created_at.date(), s.n.date())
        s.ae(s.bm.created_at.hour, s.n.hour)
        s.ae(s.bm.created_at.minute, s.n.minute)
        s.ae(s.bm.created_at.second, s.n.second)
        s.ae(s.bm2.created_at.date(), s.n2.date())
        s.ae(s.bm2.created_at.hour, s.n2.hour)
        s.ae(s.bm2.created_at.minute, s.n2.minute)
        s.ae(s.bm2.created_at.second, s.n2.second)

    def test_updated_at(s):
        s.bm.save()
        n = datetime.now()
        s.bm2.save()
        n2 = datetime.now()

        s.aii(s.bm.updated_at, type(n))

        s.ae(s.bm.updated_at.date(), n.date())
        s.ae(s.bm.updated_at.hour, n.hour)
        s.ae(s.bm.updated_at.minute, n.minute)
        s.ae(s.bm.updated_at.second, n.second)
        s.ae(s.bm2.updated_at.date(), n2.date())
        s.ae(s.bm2.updated_at.hour, n2.hour)
        s.ae(s.bm2.updated_at.minute, n2.minute)
        s.ae(s.bm2.updated_at.second, n2.second)

        s.ae(s.bm.updated_at.date(), s.bm.created_at.date())
        s.ae(s.bm.updated_at.hour, s.bm.created_at.hour)
        s.ae(s.bm.updated_at.minute, s.bm.created_at.minute)
        s.ae(s.bm.updated_at.second, s.bm.created_at.second)
        s.ae(s.bm2.updated_at.date(), s.bm2.created_at.date())
        s.ae(s.bm2.updated_at.hour, s.bm2.created_at.hour)
        s.ae(s.bm2.updated_at.minute, s.bm2.created_at.minute)
        s.ae(s.bm2.updated_at.second, s.bm2.created_at.second)

    def test_to_dict(s):
        d = s.bm.to_dict().keys()
        d2 = s.bm.to_dict()
        s.ai("id", d)
        s.ai("__class__", d)
        s.ai("created_at", d)
        s.ai("updated_at", d)

        s.aii(d2["id"], str)
        s.aii(d2["__class__"], str)
        s.aii(d2["created_at"], str)
        s.aii(d2["updated_at"], str)

    def test_str(s):
        st = s.bm.__str__()

        s.ai("[BaseModel]", st)
        s.ai("'id'", st)
        s.ai("'created_at'", st)
        s.ai("'updated_at'", st)

    def test_save(s):
        pass

    def test_load(s):
        pass

    def test_make_from_dict(s):
        pass
