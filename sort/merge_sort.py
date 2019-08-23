# -*- coding:utf-8 -*-


class MergeSort(object):
    """归并排序"""
    def __init__(self):
        pass

    @classmethod
    def sort(cls, arr):
        n = len(arr)
        if n <= 1:
            return

        cls._sort(arr, 0, n-1)

    @classmethod
    def _sort(cls, arr, l, r):
        if l >= r:
            return

        mid = (l+r)/2
        cls._sort(arr, l, mid)
        cls.sort(arr, mid, r)


        pass

    @classmethod
    def _merge(cls, arr, l, mid, r):
        pass