#sorting
#data arrangements for better efficiency or better access
n=int(input())
m=list(map(int,input().split()))
marks=[]
for i in range(n):
  marks.append(m[i])
marks.sort()
for i in marks:
    print(i,end=" ")
def student_sort(marks):
    marks.sort()
    return marks

n = int(input())
m = list(map(int, input().split()))

result = student_sort(m)
print(*result)
l=[2,3,4,5,7,8]
rollno=5
for i in range(len(l)):
    if l[i]==rollno:
        print("index",i,"rollno",l[i])

arr=[17,50,12,9,5]
target=9
arr.sort()
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
else:
    print("NOT FOUND")
    

#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i #min no. is 1st element of every unsorted array assumed
        #iterate inside unsorted array
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx=j
        
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

print(selection_sort([120,567,22,9,77,2120]))

#Sorting:Data arrangements for better access

# A training institute received student marks one by one. Write a function 
# which makes sure that the list of marks remain sorted in ascending order
# after each new marks is entered.

#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i #min no. is 1st element of every unsorted array assumed
        #iterate inside unsorted array
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx=j
        
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
arr=[]
while True:
    n=int(input())
    if n<0:
        print("final sorted list : ",arr)
        break
    arr.append(n)
    print(selection_sort(arr))  


# A fintech company processes millions of digital transactions everyday at teh end of each month the system myst generate financial report where all transaction amounts are sorted in ascending order, because the dataset is very large the order of equal transaction amounts must be preserved.
# you're given a list of integers where each integer represents a transaction amount.write the program to sort the transaction amount in ascending order using merge sort.
#  transaction amount can be +ve or -ve duplicates are not allowed and do not use built-in sort function.

# A school has a small list of student roll no's, the list is not sorted.You're asked to check whether a particular roll no exist or not.without using in
def linear_Search(arr,target):
    flag = 0
    for i in range(len(arr)):
        if arr[i] == target:
            flag = 1
    if flag:
        print("FOUND")
    else:
        print("NOT FOUND")

arr = [1,5,2,3,6,8,9]
target = 10
linear_Search(arr,target)

#or
l=[2,3,4,5,7,8]
rollno=5
for i in range(len(l)):
    if l[i]==rollno:
        print(i,l[i])

#or
def linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
target=int(input("enter target"))
print("element found at the index(-1 means element not found)-",linear([11,7,90,20,56],target))


#binary search
def binary_Search(arr,target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = int(((left+right)/2))
        if target == arr[mid]:
            return mid
        elif target <arr[mid]:
            right=mid-1
        elif target > arr[mid]:
            left = mid+1
    return -1
arr = [1,2,3,4,5,6,7,8,9]
target = 10
if binary_Search(arr,target) != -1:
    print(f"Element found at : {binary_Search(arr,target)}")
else:
    print("NOT FOUND")

#or
arr=[17,50,12,9,5]
target=9
arr.sort()
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
else:
    print("NOT FOUND")
    



# A logistics company wants to ship in d days you're given a list of package weights  and no.of days d you must find the minimum ship capacity such that all packages can be shipped in d days.

# [1,2,3,4,5,6,7,8,9,10] , 5 -> o/p = 15
# [3,2,2,4,1,4],3 ->  o/p  = 6
# [10],1 ->  O/P = 10 
#constraints 
"""
1.ship has fixed capacity per day
2.packages must be shipped in order
3.each day weight reaches the ship capacity once capacity is exceeded shipping continues next day
4.minimum capacity of weights is max weight in the list"""
def can_ship(weights,days,capacity):
    current_load = 0
    used_days = 1

    for i in weights:
        if current_load+i > capacity:
            used_days += 1
            current_load = 0
        current_load+= i
    return used_days<=days

def min_ship_capacity(weights,days):
    min_cap = max(weights)
    max_cap = sum(weights)

    answer = max_cap

    while min_cap <= max_cap:
        mid = (min_cap + max_cap)//2

        if can_ship(weights,days,mid):
            answer = mid
            max_cap = mid-1
        else:
            min_cap=mid+1
    return answer
li=[1,2,3,4,5,6,7,8,9,10]
d=5
print(min_ship_capacity(li,d))


"""
a cloud monitoring system records network traffic per min during the day the traffic data is stored as a list of integer where each integer 
represents traffic at a paticular min a traffic peak is defined as a element that i greater than its immedidate neighbour 
for boundary elements the 1st element is peak if it is greater than 2nd and the last element is peak if it is greater than 2nd last 
given a list of integer traffic find the index of any one peak element if multiple peak exisits return the index of any one of them
testcase:1[1,2,3,1] output:index->2
explanation:[1,2,3,1] index=[0,1,2,3]
3>2 and 3>1 ->peak so index is 2
2->[1 2 1 3 5 6 4] output is either  1
[10]->0 """

def peak(arr):
    left=0
    right=len(arr)-1
    while left<right:
        mid=(left+right)//2

#merge sort
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left<right:
            result.append(left)
            i+=1
        else:
            result.append(right[j])
            j+=1
    #adding of leftover elements
    result
    return result
def merge_sort(arr):
    #base case
    if len(arr)<=1:
        return arr
    #step 1 dividing
    mid=len(arr)//2
    left=merge_sort(arr[:mid])#half left part of arr
    right=merge_sort(arr[mid:])#half right part of array
    #merge the single pieces while sorting

    return merge(left,right)



