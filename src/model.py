# coding: utf-8
"""
Sample model
__author__ = 'naubull2 (naubull2@gmail.com)'
"""


class SortMachine:
    """Python bulit-in(tim sort), stalin sort"""

    def __init__(self):
        pass

    def sort(self, arr, reverse=False, method=None):
        if method is None:
            method = "default"

        if method == "stalin":
            ret = []
            for i in range(len(arr)):
                if i == 0:
                    ret.append(arr[i])
                elif arr[i] > ret[-1]:
                    ret.append(arr[i])
            if reverse:
                return ret[::-1]
            return ret
        else:
            return sorted(arr, reverse=reverse)
