#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    if my_list:
        new_list = [element*number for element in my_list]
    return new_list