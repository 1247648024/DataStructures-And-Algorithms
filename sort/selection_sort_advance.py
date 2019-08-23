# -*- coding:utf-8 -*-


from sort.sort_test_helper import SortTestHelper


class SelectionSort(object):
    """选择排序 优化"""
    def __init__(self):
        pass

    @classmethod
    def sort(cls, arr):
        arr_len = len(arr)
        # 在每一轮中, 可以同时找到当前未处理元素的最大值和最小值
        left = 0
        right = arr_len - 1
        while left < right:
            min_index = left
            max_index = right

            # 在每一轮查找时，要保证arr[min_index] <= arr[max_index]
            if arr[max_index] < arr[min_index]:
                cls.swap(arr, min_index, max_index)

            for i in range(left+1, right):
                if arr[i] < arr[min_index]:
                    min_index = i
                elif arr[max_index] < arr[i]:
                    max_index = i

            cls.swap(arr, left, min_index)
            cls.swap(arr, right, max_index)

            left += 1
            right -= 1

    @classmethod
    def swap(cls, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":

    n = 10000
    int_random_arr = SortTestHelper.generate_random_array(n, 0, 10000)
    int_random_arr_cpoy = int_random_arr.copy()
    SortTestHelper.test_sort("sort.selection_sort_using_comparable", "SelectionSort", int_random_arr)
    SortTestHelper.print_array(int_random_arr)

    SortTestHelper.test_sort("sort.selection_sort_advance", "SelectionSort", int_random_arr_cpoy)
    SortTestHelper.print_array(int_random_arr_cpoy)