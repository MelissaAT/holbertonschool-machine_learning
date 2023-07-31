#!/usr/bin/env python3
"""Documentation """
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates two matrices
    along a specific axis"""
    concatenated_matrix = np.concatenate((mat1, mat2), axis=axis)
    return concatenated_matrix
