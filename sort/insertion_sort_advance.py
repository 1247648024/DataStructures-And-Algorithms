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
            e = arr[i]
            index = i
            for j in range(i, 0, -1):
                if e < arr[j-1]:
                    arr[j] = arr[j-1]
                    index = j-1
                else:
                    # j之前的数据都比arr[j]小，则提前终止
                    break

            # 此时index位置就是arr[i]应该放的位置
            arr[index] = e

    @classmethod
    def swap(cls, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    # 比较SelectionSort和InsertionSort两种排序算法的性能效率
    # 优化后，插入排序比选择排序性能略好
    # 对于有序性强的数组，插入排序远远优于选择排序

    n = 10000

    # 一般测试
    print("Test for random array, size = " + str(n) + " , random range [0, " + str(n) + "]")
    int_arr = SortTestHelper.generate_random_array(n, 0, 10000)
    int_arr_copy = int_arr.copy()

    SortTestHelper.test_sort("sort.selection_sort_using_comparable", "SelectionSort", int_arr)  # 大约 11s
    SortTestHelper.print_array(int_arr)
    SortTestHelper.test_sort("sort.insertion_sort_advance", "InsertionSort", int_arr_copy)  # 大约 9.7s
    SortTestHelper.print_array(int_arr_copy)

    # 有序性更强的测试
    print("Test for more ordered random array, size = " + str(n) + " , random range [0, " + str(3) + "]")
    int_arr = SortTestHelper.generate_random_array(n, 0, 3)
    int_arr_copy = int_arr.copy()

    SortTestHelper.test_sort("sort.selection_sort_using_comparable", "SelectionSort", int_arr)  # 大约 11s
    SortTestHelper.print_array(int_arr)
    SortTestHelper.test_sort("sort.insertion_sort_advance", "InsertionSort", int_arr_copy)  # 大约 6.6s
    SortTestHelper.print_array(int_arr_copy)

    # 测试近乎有序的数组
    print("Test for more ordered random array, size = " + str(n) + " , random range [0, " + str(10000) + "]")
    int_arr = SortTestHelper.generate_nearly_ordered_array(n, 100)
    int_arr_copy = int_arr.copy()

    SortTestHelper.test_sort("sort.selection_sort_using_comparable", "SelectionSort", int_arr)  # 大约 3.3s
    SortTestHelper.print_array(int_arr)
    SortTestHelper.test_sort("sort.insertion_sort_advance", "InsertionSort", int_arr_copy)  # 大约 0.005s
    SortTestHelper.print_array(int_arr_copy)