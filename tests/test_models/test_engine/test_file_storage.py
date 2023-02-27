#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        fs = FileStorage()
        self.assertEqual(fs.__file_path, "savefile.json")

    def test_objects(self):
        fs = FileStorage()
        self.assertEqual(type(fs.__objects), dict)

    def test_all(self):
        fs = FileStorage()
        self.assertEqual(fs.all(), fs.__objects)

    def test_new(self):
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        self.assertEqual(fs.all(), fs.__objects)

    def test_save(self):
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        fs.save()
        self.assertEqual(fs.all(), fs.__objects)

    def test_reload(self):
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        fs.save()
        fs.reload()
        self.assertEqual(fs.all(), fs.__objects)

    def test_base_model(self):
        bm = BaseModel()

    def test_base_save(self):
        bm = BaseModel()
