# -*- coding:utf-8 -*-

import numpy as np
import importlib
import time


class SortTestHelper(object):
    """排序测试辅助类"""
    def __init__(self):
        pass

    @classmethod
    def generate_random_array(cls, n, l, r):
        """生成有n个元素的随机数组,每个元素的随机范围为[l, r]"""
        assert l <= r

        # 此处生成随机数组借助numpy工具包

        return np.random.randint(low=l, high=r, size=n)

    @classmethod
    def generate_nearly_ordered_array(cls, n, swap_times):
        arr = [i for i in range(n)]
        for t in range(swap_times):
            indexes = np.random.randint(low=0, high=n-1, size=2)
            temp = arr[indexes[0]]
            arr[indexes[0]] = arr[indexes[1]]
            arr[indexes[0]] = temp

        return arr

    @classmethod
    def print_array(cls, arr):
        """打印arr的所有内容"""
        print(" ".join(str(i) for i in arr))
        print("\n")

    @classmethod
    def test_sort(cls, sort_module_name, sort_class_name, arr):
        """测试sort_name所对应的排序算法排序arr数组的算法运行时间"""
        try:
            # 反射获取排序的Class
            sort_module = importlib.import_module(sort_module_name)
            sort_class = getattr(sort_module, sort_class_name)
            start_time = time.time()
            sort_class.sort(arr)
            print("{0}.{1} used time: {2}".format(sort_module_name, sort_class_name, time.time() - start_time))
        except Exception as e:
            raise Exception("{0} exception !! e: {1}".format((sort_class_name, e)))

