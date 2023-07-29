#!/usr/bin/env python3
"""Documentation"""


def cat_arrays(arr1, arr2):
    """concatenate two arrays"""
    conc_list = []
    for i in arr1:
        conc_list.append(i)
    for i in arr2:
        conc_list.append(i)
    return conc_list
