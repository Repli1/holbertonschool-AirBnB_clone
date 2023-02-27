#!/usr/bin/python3
"""Define a class Filestorage"""
import json
from os import path


class FileStorage:
    """Class"""
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
      from models.amenity import Amenity
      from models.city import City
      from models.state import State
      from models.review import Review
      from models.place import Place
      dict_of_class = {
        "BaseModel": BaseModel,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
        }
      FileStorage.__objects.clear()
      storage_copy = {}
      if path.exists(FileStorage.__file_path):
          with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            storage_copy = json.load(f)
      for key, value in storage_copy.items():
          #split the 1st key that is the class_name.id and take only the class_name
          class_name = key.split(".")[0]
          if class_name in dict_of_class:
              cls = dict_of_class[class_name]
              storage_copy[key] = cls(**value)
      FileStorage.__objects = storage_copy
