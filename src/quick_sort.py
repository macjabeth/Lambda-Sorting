l = [1, 2, 1]

def partition(l):
    pivot = l[0]
    # <= here so we can include values that are equal to the pivot
    # but we slice at the second (1) index to ensure the pivot is not included
    left = [i for i in l[1:] if i <= pivot]
    right = [i for i in l if i > pivot]
    return left, pivot, right

def quicksort(l):
    # base case
    if len(l) <= 1: return l
    # grab left/right partitions
    # pivot is the catalyst
    left, pivot, right = partition(l)
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(l))
