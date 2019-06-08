# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for item in arr:
    if item == target: return True
  return False   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0: return False # array empty
  low = 0
  high = len(arr)-1
  while low <= high:
    middle = (low+high) // 2
    if arr[middle] == target:
      return True
    elif arr[middle] < target:
      low = middle + 1
    elif arr[middle] > target:
      high = middle - 1
  return False # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if len(arr) == 0: return False # array empty  
  if low > high: return False
  middle = (low+high)//2
  if arr[middle] == target:
    return True
  elif arr[middle] < target:
    return binary_search_recursive(arr, target, middle+1, high)
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle-1)
