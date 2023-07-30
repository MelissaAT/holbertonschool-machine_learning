#!/usr/bin/env python3
"""Documentation"""
def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        new_matrix = mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        new_matrix = []
    for row1, row2 in zip(mat1, mat2):
        new_row = row1 + row2
        new_matrix.append(new_row)

   

    return new_matrix

