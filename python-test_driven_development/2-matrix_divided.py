#!/usr/bin/python3
"""Module de fonctions mathématiques"""


def matrix_divided(matrix, div):
    """function that divide two variables"""
    rows = len(matrix)
    columns = len(matrix[0])

    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise ValueError("Each row of the matrix must have the same size")
    new_matrix = []
    for x in range(rows):
        row = []
        for y in range(columns):
            num = matrix[x][y]
            if num is None or not isinstance(num, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif div is None or not isinstance(div, (float, int)):
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                row.append(float("{:.2f}".format(matrix[x][y] / div)))
            new_matrix.append(row)
    return new_matrix
