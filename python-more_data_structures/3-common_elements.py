#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    for element in set_1:
        if element in set_2:
            return list(element)
        else:
            return
