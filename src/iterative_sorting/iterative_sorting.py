# TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     count = len(arr)
#     # loop through n-1 elements
#     for i in range(count-1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         for j in range(cur_index, count):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j
#         # TO-DO: swap
#         arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
#     return arr


def selection_sort(arr):
    count = len(arr)
    # repeat arr[n-1] times
    for i in range(count-1):
        # set first element as minimum
        min_value = i
        # for each unsorted element
        for j in range(i, count):
            # if element is less than current minimum
            if arr[j] < arr[min_value]:
                # set element as new minimum
                min_value = j
        # swap minimum with first element position
        arr[min_value], arr[i] = arr[i], arr[min_value]
    # return sorted array
    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     count = len(arr)
#     for i in range(count):
#         for j in range(count-1):
#             if arr[j+1] < arr[j]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr


def bubble_sort(arr):
    count = len(arr)-1
    swapped = True
    while swapped:
        # reset swapped value
        swapped = False
        for i in range(count):
            # is left element greater than right element?
            if arr[i] > arr[i+1]:
                # swap and update status
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    # return sorted array
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
