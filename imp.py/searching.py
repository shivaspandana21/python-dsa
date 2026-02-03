#binary search
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    #loop until search space is vaild
    while low<=high:
        mid=(low+high)//2 #to find mid of arr
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:#target in the right 
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,3,4,5,6,7,8,9]
target=6
print(binary_search(arr,target))

#linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[1,2,3,4,5,6,7,8,9]
target=8
print(linear_search(arr,target))