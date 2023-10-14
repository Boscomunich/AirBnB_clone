#!/usr/bin/python3
"""
BaseModel class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models
import json
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
        BaseModel: The base or parent class for all the classes
        Features:
        id - the unique identification of the object
        created_at - the datetime in which the object was created
        updated_at - the datetime in which the object was modified
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the base model class
            id - the unique identification of the object
            created_at - the datetime in which the object was created
            updated_at - the datetime in which the object was modified
        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                elif key == "__class__":
                    pass
                elif key != "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """"This method returns a string of object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save method that updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_obj_dict = self.__dict__.copy()
        new_obj_dict["__class__"] = self.__class__.__name__
        new_obj_dict["created_at"] = self.created_at.isoformat()
        new_obj_dict["updated_at"] = self.updated_at.isoformat()
        return new_obj_dict
