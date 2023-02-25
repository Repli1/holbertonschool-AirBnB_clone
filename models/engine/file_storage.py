#!/usr/bin/python3
""""""
import json
from os import path

class FileStorage:
    """"""
    __file_path = "savefile.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    def save(self):
        storage_copy = FileStorage.__objects.copy()
        for key, value in storage_copy.items():
            storage_copy[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(storage_copy, f)
    def reload(self):
        from models.base_model import BaseModel
        FileStorage.__objects.clear()
        storage_copy = {}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
              storage_copy = json.load(f)
        for key, value in storage_copy.items():
            storage_copy[key] = BaseModel(**value)
        FileStorage.__objects = storage_copy
