#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""define a class Base model"""


class BaseModel:
    """initializate """
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) > 0:
            for key, v in kwargs.items():
                if key == 'id':
                    self.id = str(v)
                if key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(v)
                if key == 'created_at':
                    self.created_at = datetime.fromisoformat(v)
        else:
            no_str_id = uuid.uuid4()
            self.id = str(no_str_id)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """update the atribute update_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dict from the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = (self.created_at).isoformat()
        instance_dict['updated_at'] = (self.updated_at).isoformat()
        return instance_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
