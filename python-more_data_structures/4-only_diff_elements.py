#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    if not set_1 and not set_2:
        return diff
    if not set_1:
        return set_2
    if not set_2:
        return set_1
    for element in set_1:
        if element not in set_2:
            diff.append(element)
    for element in set_2:
        if element not in set_1:
            diff.append(element)
    return(diff)
