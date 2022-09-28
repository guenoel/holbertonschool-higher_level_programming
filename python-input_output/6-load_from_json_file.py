#!/usr/bin/python3
"""Commentaire de module"""

import json


def load_from_json_file(filename):
    """Commentaire de méthode"""
    with open(filename, mode="r", encoding='utf-8') as a_file:
        return json.load(a_file)
