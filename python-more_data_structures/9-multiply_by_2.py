#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dico = {}
    if a_dictionary:
        for element in a_dictionary:
            new_dico[element] = (a_dictionary[element] * 2)
    return new_dico
