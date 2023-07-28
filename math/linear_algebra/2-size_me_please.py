#!/usr/bin/env python3

"""Documentation"""

def matrix_shape(matrix):
    """Shape of a matrix"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
