l = [1, 2, 1]

def partition(l):
    pivot = l[0]
    left = [i for i in l[1:] if i <= pivot]
    right = [i for i in l if i > pivot]
    return left, pivot, right

def quicksort(l):
    if len(l) <= 1: return l
    left, pivot, right = partition(l)
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(l))
