#!/usr/bin/python3
"""Module de fonctions mathématiques"""


def matrix_divided(matrix, div):
    """function that divide two variables"""
    rows = len(matrix)
    columns = len(matrix[0])

    if type(div) is not int and type(div) is not float:
        raise ValueError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise ValueError("Each row of the matrix must have the same size")
    new_matrix = []
    for x in range(rows):
        row = []
        for y in range(columns):
            if y is None or type(y) is not int and type(y) is not float or y != y:
                raise TypeError("All element of the matrix must be integer")
            elif div is None or type(div) is not int and type(div) is not float or div != div:
                raise TypeError("div must be an integer")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                row.append(float("{:.2f}".format(matrix[x][y] / div)))
        new_matrix.append(row)
    return new_matrix
