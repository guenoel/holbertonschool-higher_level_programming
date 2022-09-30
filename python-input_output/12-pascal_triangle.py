#!/usr/bin/python3
""" My module comment
"""


def pascal_triangle(n):
    """return pascal triangle

    Args:
        n (int): height of the triangle

    Returns:
        table of table
    """
    lol = []
    y = 0
    if n <= 0:
        return my_list
    lol = [[0 for x in range(i + 1)] for i in range(n)]
    lol[0] = [1]
    for x in range(1, n):
        lol[x][0] = 1
        for y in range(1, x + 1):
            if y < len(lol[x - 1]):
                lol[x][y] = lol[x - 1][y - 1] + lol[x - 1][y]
            else:
                lol[x][y] = lol[x - 1][0]
    return (lol)
