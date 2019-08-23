# -*- coding:utf-8 -*-


from sort.sort_test_helper import SortTestHelper


class InsertionSort(object):
    """插入排序：类似排序扑克牌，从前往后排序，每拿出一张牌插入它前方合适的位置"""
    def __init__(self):
        pass

    @classmethod
    def sort(cls, arr):
        arr_len = len(arr)
        for i in range(arr_len):

            # 寻找元素arr[i]合适的插入位置
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    cls.swap(arr, j, j-1)
                else:
                    # j之前的数据都比arr[j]小，则提前终止
                    break

    @classmethod
    def swap(cls, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    n = 10000
    print("Test for random array, size = " + str(n) + " , random range [0, " + str(n) + "]")

    int_arr = SortTestHelper.generate_random_array(n, 0, 10000)
    int_arr_copy = int_arr.copy()

    # 比较SelectionSort和InsertionSort两种排序算法的性能效率
    # 此时，插入排序比选择排序性能略低，因为每次寻找arr[i]的位置时，都是挨个往前比较、交换，其中交换有三步操作，比较耗时

    SortTestHelper.test_sort("sort.selection_sort_using_comparable", "SelectionSort", int_arr)
    SortTestHelper.print_array(int_arr)
    SortTestHelper.test_sort("sort.insertion_sort", "InsertionSort", int_arr_copy)
    SortTestHelper.print_array(int_arr_copy)