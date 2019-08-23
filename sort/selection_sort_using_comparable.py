# -*- coding:utf-8 -*-

from sort.sort_test_helper import SortTestHelper


class SelectionSort(object):
    """选择排序 comparable"""
    def __init__(self):
        pass

    @classmethod
    def sort(cls, arr):
        arr_len = len(arr)
        for i in range(arr_len):
            # 寻找[i, n)区间里的最小值的索引
            min_index = i
            for j in range(i + 1, arr_len):
                if arr[j] < arr[min_index]:
                    min_index = j

            SelectionSort.swap(arr, i, min_index)

    @classmethod
    def swap(cls, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


class Student(object):
    """自定义Student 用于比较排序"""

    def __init__(self, name, core):
        self._name = name
        self._core = core
        pass

    @property
    def name(self):
        return self._name

    @property
    def core(self):
        return self._core

    """重载Student 的小于运算符"""
    def __lt__(self, other):
        if self._core < other.core:
            return 1
        elif self._core > other.core:
            return 0
        else:
            if self._name < other.name:
                return 1
            else:
                return 0

    # 重载Student的print
    def __str__(self):
        return "<name: {0}, core: {1}>".format(self._name, self._core)


if __name__ == "__main__":

    # 测试int
    int_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    SelectionSort.sort(int_arr)
    print("int_arr === ", int_arr)

    # 测试double
    double_arr = [10.1, 9.1, 8.1, 7.1, 6.1, 5.1, 4.1, 3.1, 2.1, 1.1]
    SelectionSort.sort(double_arr)
    print("double_arr === ", double_arr)

    # 测试自定义的类 Student
    stu_arr = [
        Student("D", 90),
        Student("C", 100),
        Student("B", 95),
        Student("A", 95)
    ]
    SelectionSort.sort(stu_arr)
    for stu in stu_arr:
        print(stu)

    # 测试排序算法辅助函数
    n = 2000
    int_random_arr = SortTestHelper.generate_random_array(n, 0, 10000)
    SortTestHelper.test_sort("sort.selection_sort_using_comparable", "SelectionSort", int_random_arr)
    SortTestHelper.print_array(int_random_arr)


