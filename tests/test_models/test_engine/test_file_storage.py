#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_file_path:
        fs = FileStorage()
        self.assertEqual(fs.__file_path, "savefile.json")

    def test_objects:
        fs = FileStorage()
        self.assertEqual(type(fs.__objects), dict)

    def test_all:
        fs = FileStorage()
        self.assertEqual(fs.all(), fs.__objects)

    def test_new:
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        self.assertEqual(fs.all(), fs.__objects)

    def test_save:
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        fs.save()
        self.assertEqual(fs.all(), fs.__objects)

    def test_reload:
        bm = BaseModel()
        fs = FileStorage()
        fs.new(bm)
        fs.save()
        fs.reload()
        self.assertEqual(fs.all(), fs.__objects)

    def test_base_model:
        bm = BaseModel()

    def test_base_save:
        bm = BaseModel()
