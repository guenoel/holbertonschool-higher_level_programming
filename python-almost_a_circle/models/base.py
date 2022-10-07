#!/usr/bin/python3
"""Commentaire de module"""

import json
import os


class Base:
    """Class base ... no comments"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """methode that return a json string from a list of dict"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(cls.__name__+".json", "w") as file:
                file.write([])
            file.close()
        else:
            dict_objs = [obj.to_dictionary() for obj in list_objs]
            # for obj in list_objs:
            #     dict_objs = obj.to_dictionary()
            with open(cls.__name__+".json", "w") as file:
                file.write(cls.to_json_string(dict_objs))
            file.close()

    def from_json_string(json_string):
        """Method that return a string from a JSon file"""
        list_of_dico = []
        if json_string and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            list_of_dico = json.loads(json_string)
        return list_of_dico

    @classmethod
    def create(cls, **dictionary):
        """Method that update attributes of an instance"""
        if cls.__name__ == "Rectangle":
            my_rectangle = cls(1, 1)
        if cls.__name__ == "Square":
            my_rectangle = cls(1)
        my_rectangle.update(**dictionary)
        return my_rectangle

    @classmethod
    def load_from_file(cls):
        """Method that create a list dict of instances"""
        filename = cls.__name__ + ".json"
        list_of_dict = []
        l=[]
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                s = file.read()
                list_of_dict = cls.from_json_string(s)
                [l.append(cls.create(**dico)) for dico in list_of_dict]
            return l
