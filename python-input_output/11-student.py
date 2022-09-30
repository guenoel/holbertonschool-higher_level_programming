#!/usr/bin/python3
""" My module comment
"""


class Student:
    """ My class student
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = dict()

        if type(attrs) is list and all(isinstance(ele, str) for ele in attrs):
            for ele in attrs:
                if ele in self.__dict__:
                    my_dict.update({ele: self.__dict__[ele]})
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for ele in json:
            self.__dict__.update({ele: json[ele]})
