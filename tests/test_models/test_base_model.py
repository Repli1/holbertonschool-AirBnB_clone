#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        bm = BaseModel()
        bm.save()
        key = f"{bm.__class__.__name__}.{bm.id}"
        obj_dict = storage.all()[key].to_dict()
        self.assertEqual(bm.updated_at.isoformat(), obj_dict['updated_at'])

    def test_to_dict(self):
        bm = BaseModel()
        new_dict = bm.to_dict()
        self.assertEqual(new_dict['__class__'], bm.__class__.__name__)
        self.assertEqual(new_dict['created_at'], (bm.created_at).isoformat())
        self.assertEqual(new_dict['updated_at'], (bm.updated_at).isoformat())

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
