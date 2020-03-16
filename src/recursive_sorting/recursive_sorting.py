# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # TO-DO
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    if i == len(arrA):
        merged_arr.extend(arrB[j:])
    else:
        merged_arr.extend(arrA[i:])
    return merged_arr


arrA = [5, 6, 3, 4, 8]
arrB = [1, 6, 7, 2, 3, 9]
print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        a = merge_sort(arr[0:mid])
        b = merge_sort(arr[mid:])
        arr = merge(a, b)
    return arr


arr = [1, 6, 0, 47, 9, 21]
print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
