# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    result = []
    arrAlen, arrBlen = len(arrA), len(arrB)
    arrAindex, arrBindex = 0, 0
    while arrAindex < arrAlen and arrBindex < arrBlen:
        if arrA[arrAindex] < arrB[arrBindex]:
            result.append(arrA[arrAindex])
            arrAindex += 1
        else:
            result.append(arrB[arrBindex])
            arrBindex += 1
    result = result + arrA[arrAindex:] + arrB[arrBindex:]
    print(arrA, arrB, '=', result)
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    arrA = arr[:middle]
    arrB = arr[middle:]
    print('left:', arrA)
    print('right:', arrB)

    return merge(
        merge_sort(arrA),
        merge_sort(arrB)
    )


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
