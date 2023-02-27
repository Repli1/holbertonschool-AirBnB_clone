#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    def test_save_and_reload(self):
        model_id = uuid.uuid4()
        u_at = "2018-06-14T22:31:03.285259"
        c_at = "2018-06-14T22:31:03.285255"
        bm = BaseModel(id=model_id, updated_at=u_at, created_at=c_at)
        fs = FileStorage()
        old_dict = fs._FileStorage__objects.copy()
        fs.new(bm)
        fs.save()
        new_dict1 = fs._FileStorage__objects.copy()
        fs._FileStorage__objects.clear()
        fs.reload()
        new_dict2 = fs._FileStorage__objects.copy()
        self.assertEqual(new_dict1.keys(), new_dict2.keys())
        self.assertNotEqual(old_dict, new_dict1)
   
    def test_file_path(self):
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__file_path, "savefile.json")

    def test_objects(self):
        fs = FileStorage()
        self.assertEqual(type(fs._FileStorage__objects), dict)

    def test_all(self):
        fs = FileStorage()
        self.assertEqual(fs.all(), fs._FileStorage__objects)

    def test_new(self):
        model_id = uuid.uuid4()
        u_at = "2017-06-14T22:31:03.285259"
        c_at = "2017-06-14T22:31:03.285255"
        bm = BaseModel(id=model_id, updated_at=u_at, created_at=c_at)
        fs = FileStorage()
        old_dict = fs._FileStorage__objects.copy()
        key = f"{bm.__class__.__name__}.{bm.id}"
        self.assertNotIn(key, old_dict.keys())
        fs.new(bm)
        new_dict = fs._FileStorage__objects
        self.assertIn(key, new_dict.keys())
        self.assertEqual(new_dict[key], bm)
        self.assertNotEqual(old_dict, new_dict)
