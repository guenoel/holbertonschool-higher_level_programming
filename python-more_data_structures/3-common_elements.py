#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    if not set_1 or not set_2:
        return common
    for element in set_1:
        if element in set_2:
            common.append(element)
    return common
