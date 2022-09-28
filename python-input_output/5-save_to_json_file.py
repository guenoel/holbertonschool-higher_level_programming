#!/usr/bin/python3
"""Commentaire de module"""

import json


def save_to_json_file(my_obj, filename):
    """Commentaire de méthode"""
    with open(filename, mode="w", encoding='utf-8') as a_file:
        return json.dump(my_obj, a_file)
