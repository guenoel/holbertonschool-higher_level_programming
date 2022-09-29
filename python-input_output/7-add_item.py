#!/usr/bin/python3
"""Commentaire de module"""


import json
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if path.exists('add_item.json'):
    my_list = load_from_json_file('add_item.json')

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        my_list.append(elem)

save_to_json_file(my_list, 'add_item.json')
