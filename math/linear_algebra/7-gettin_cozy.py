#!/usr/bin/env python3
"""Documentation"""
import numpy as np

def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        new_matrix = np.concatenate((mat1, mat2), axis=0)
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        new_matrix = np.concatenate((mat1, mat2), axis=1)

    return new_matrix.tolist()
