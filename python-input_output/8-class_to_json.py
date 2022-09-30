#!/usr/bin/python3
"""Commentaire de module"""

import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
