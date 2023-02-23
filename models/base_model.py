#!/usr/bin/python3
import uuid
import datetime
"""define a class Base model"""


class BaseModel:
    """initializate """
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) > 0:
            for key, v in kwargs.items():
                if key == 'id':
                    id_str = str(v)
                if key == 'update_at':
                    update_at = v.isoformat()
                if key == 'created_at':
                    created_at = v.isoformat()

        else:
            no_str_id = uuid.uuid4
            id_str = str(no_str_id)
            created_at = datetime.now()
            updated_at = datetime.now()

    def save(self):
        """update the atribute update_at"""
        update_at = datetime.now()

    def to_dict(self):
        """return a dict from the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = (self.created_at).isoformat()
        instance_dict['updated_at'] = (self.updated_at).isoformat()
        return instance_dict

    def __str__(self):
        return f"[<{self.__class__.__name__}>] (<{self.id_str}>) <{self.__dict__}>"
