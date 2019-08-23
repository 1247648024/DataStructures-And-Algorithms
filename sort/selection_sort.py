# -*- coding:utf-8 -*-


class SelectionSort(object):
    """选择排序"""
    def __init__(self):
        pass

    @classmethod
    def sort(cls, arr):
        arr_len = len(arr)
        for i in range(arr_len):
            # 寻找[i, n)区间里的最小值的索引
            min_index = i
            for j in range(i+1, arr_len):
                if arr[j] < arr[min_index]:
                    min_index = j

            cls.swap(arr, i, min_index)

    @classmethod
    def swap(cls, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


if __name__ == "__main__":
    int_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    SelectionSort.sort(int_arr)

    print("int_arr === ", int_arr)