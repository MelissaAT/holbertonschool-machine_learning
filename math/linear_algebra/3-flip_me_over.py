#!/usr/bin/env python3
"""Documentation"""


def matrix_transpose(matrix):
    """trasponse of a 2D matrix"""
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        new_matrix.append(row)

    return new_matrix
