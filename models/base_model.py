#!/usr/bin/python3
"""
Base Module - defines all common attributes/methods for other classes
"""

import datetime
import uuid


class BaseModel():
    """Defines the base for other classes to inherit"""

    def __init__(self):
        """Initializes an object with its attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """Returns the string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        obj_dict = vars(self)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
