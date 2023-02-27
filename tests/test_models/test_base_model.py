#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        bm = BaseModel()
        old_date = bm.updated_at
        bm.save()
        new_date = bm.updated_at
        self.assertNotEqual(old_date, new_date)

    def test_to_dict(self):
        bm = BaseModel()
        new_dict = bm.to_dict()
        self.assertEqual(type(new_dict), dict)

    def test_id(self):
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertEqual(type(bm.id), str)
        self.assertNotEqual(bm.id, bm2.id)

    def test_created_at(self):
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.created_at, bm2.created_at)

    def test_str(self):
        bm = BaseModel()
        str1 = bm.__str__()
        str2 = f"[{bm.__class__.__name__}] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str1, str2)
