#merge sort
"""def merge_sort(arr):
    # base condition: single element is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2          # find middle index

    # divide the array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # compare elements of both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # copy remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result"""

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    #to compare both halves
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #copy remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[100,22,3,40,5,60,7]
merge_sort(arr)
print(merge_sort(arr))

def quick_sort(arr, low, high):
    if low < high:
        # find pivot index after partition
        p = partition(arr, low, high)

        # recursively sort left and right subarrays
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[high]     # choose last element as pivot
    i = low - 1           # pointer for smaller element

    for j in range(low, high):
        # if current element is smaller than pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1          # return pivot index
