#!/usr/bin/env python3
"""Documentation"""


def np_elementwise(mat1, mat2):
    """performs element-wise addition, subtraction, multiplication, and division"""
    sum_result = mat1 + mat2
    diff_result = mat1 - mat2
    product_result = mat1 * mat2
    quotient_result = mat1 / mat2
    return sum_result, diff_result, product_result, quotient_result
