#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary and key:
        a_dictionary.update({key:value})
    return a_dictionary

