#!/usr/bin/python3
from inspect import isclass


def is_same_class(obj, a_class):
    """class qui verifie si c'est exactement de cette classe"""
    return type(obj) is a_class
