# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    result = []
    arrAlen, arrBlen = len(arrA), len(arrB)
    arrAindex, arrBindex = 0, 0
    # is the left (arrA) index less than its length
    # and the right (arrB) index less than its length
    while arrAindex < arrAlen and arrBindex < arrBlen:
        # compare left item to right item
        if arrA[arrAindex] < arrB[arrBindex]:
            # if less than, push left item
            result.append(arrA[arrAindex])
            arrAindex += 1
        else:
            # otherwise push right item (since it is smaller)
            result.append(arrB[arrBindex])
            arrBindex += 1
    # yeet that yeast
    print('-' * 80)
    print('>', arrA, arrB)
    print('>', result, arrA[arrAindex:], arrB[arrBindex:])
    result = result + arrA[arrAindex:] + arrB[arrBindex:]
    print('>', result)
    print('-' * 80)
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # find the middle
    middle = len(arr) // 2
    # slice list into LHS + RHS
    arrA = arr[:middle]
    arrB = arr[middle:]
    print('left:', arrA)
    print('right:', arrB)

    # split both halves again w/ recursion
    # until everything is 1 item
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
