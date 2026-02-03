"""# AN online exam system assigns each student a rollnumber from 1 to n due to a system bug one roll number is assign 
twice and one is missing you are given list of size n+1 where numbers are in rsnge 1 to n only one number is duplicated you must not modify the 
list use constant extra space find the duplicate number 
(1,3,4,2,2) o/p:2 and (3,1,3,4,2) o/p:3 and (1,1) o/p:1"""
l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i])
        else:
            continue


#floyd's tortoise and hare algorithm
def findDuplicate(num):
    slow=num[0]
    fast=num[0]
    #detecting cycle
    while True:
        if fast>=len(num) or num[fast]>=len(num):
            return "None"
        slow=num[slow]
        fast=num[num[fast]]
        if slow==fast:
            #then we have cycle
            break
    #finding the duplicate num
    slow=num[0]
    while slow!=fast:
        slow=num[slow]
        fast=num[fast]
    return slow
print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([1,1]))
#a stock analysis tool daily stock prices for each day you want to know the next day 
# when the price is higher if no higher price exists return -1 for each element in the list find the next greater element on the right
#[4,5,2,25] output:[5 25 25 -1]
# [13 7 6 12] output:[-1 ,12 ,12 ,-1]
#[5] output: [-1]
def next_greater_element(arr):
    stack = []
    n = len(arr)
    result = [-1] * n

    for i in range(n - 1, -1, -1):
        # Remove smaller or equal elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack not empty, top is next greater
        if stack:
            result[i] = stack[-1]

        # Push current element
        stack.append(arr[i])

    return result
print(next_greater_element([4,5,2,25]))
#or
# finding next grater element (momotonus stack)

def next_large_num(num):
    stack=[]#storing the index of the element which is not yet found
    result=[-1]*len(num)#initially all elements are -1
    for i in range(len(num)):
        #while stack is not empty,And currebt>existing
        while stack and num[i]>num[stack[-1]]:
            #pop the index at the top of stack
            index=stack.pop()
            #current iss greater element,so print it in result
            result[index]=num[i]
        #push current index onto stack
        stack.append(i)
    return result

print(next_large_num([4,5,2,25]))
print(next_large_num([13,7,6,12]))
#a salaray processing system manages montly bonus you are given n employees index to n-1 a list of bonus
#  update operation each operation is the form [start_index,end_index,bonus_amount] 
# this means add bonus amount to all employees from start index to end index inclusive after applying bonus updates return the final bonus array
#step2 applying the updates
def bonus_updates(n,updates):
    bonus=[0]*n
    for update in updates:
        start,end,amount=update
        bonus[start]+=amount
        if end+1<n:
            bonus[end+1]-=amount
    #step 3 calculating the final bonus using prefix sum
    for i in range(1,n):
        bonus[i]+=bonus[i-1]
    return bonus
print(bonus_updates(5,[[1,3,100],[2,4,50],[0,2,20]]))

#or
def range_update(n,updates):
    #step-1 : create empty list
    diff=[0]*n

    #step-2 : Applying the updates
    for i in updates:
        if len(i)==0:
            continue
        start=i[0]
        end=i[1]
        amount=i[2]
        diff[start]+=amount

        #step-3 : if end+1 exists
        if end+1<n:
            diff[end+1]-=amount
        
        #step-4 : keep iterating until end of tasks

    #step-5 : build the final array using prefix sum
    result=[0]*n
    result[0]=diff[0] #becoz 1st element has no prefix

    for i in range(1,n):
        result[i]=result[i-1]+diff[i]

    #step-6 : return final result
    return result

print(range_update(5,[[1,3,100],[2,4,50],[0,2,20]]))
"""# An infrastructure company is analysing rooftop heights in a city after heavy rainnfall 
water gets trped btw building each buildingg width is 1unit u are give a list of building heights 
calculate how much total rain water can be traped 
[0,1,0,2,1,0,1,3,2,1,2,] o/p:6 and [4,2,0,3,2,5] o/p:9 and [1,1,0] o/p:"""
def trap_rainwater(arr):
    left=1
    right=len(arr)-2
    lmax=arr[left-1]
    rmax=arr[right+1]
    res=0
    while left <= right :
        #if lmax is smaller,then we can decide water for arr[right]
        if rmax <= lmax :
            #added water of arr[right]
            res+=max(0,rmax-arr[right])
            #update rmax
            rmax=max(rmax,arr[right])
            #update right pointer 
            right-=1
        else:
            #add water for arr[left]
            res+=max(0,lmax-arr[left])
            #update lmax
            lmax=max(lmax,arr[left])
            #update left
            left += 1
    return res

arr=[4,2,0,3,2,5]

print(trap_rainwater(arr))


#merse sort
#divide and conquer
#*Merge Sort Without Recursion*

# Merge Sort (Transaction of e-commerce)
def merge_sort(arr):
    n=len(arr)
    temp=[0]*n
    size=1 # initial size of subarray

    while size<n:
        # choosing the start point of left subarray
        for left_start in range(0,n,2*size):
            mid=min(left_start+size,n)
            right_end=min(left_start+2*size,n)

            # merging 2 sorted subarray
            
            i=left_start # left sub array
            j=mid # right sub array
            k=left_start # point to temp index

            while i<mid and j<right_end:
                if arr[i]<=arr[j]:
                    temp[k]=arr[i]
                    i+=1
                else:
                    temp[k]=arr[j]
                    j+=1
                k+=1

            #copy the remaining element of sub array
            while i<mid:
                temp[k]=arr[i]
                i+=1
                k+=1
            
            #copy the remaining element of sub array
            while j<right_end:
                temp[k]=arr[j]
                j+=1
                k+=1
        for i in range(n):
            arr[i]=temp[i]

        size*=2
    
    return arr



arr=[17,12,5,30,4]
print(merge_sort(arr))


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


#trapping rain water problem
def traprainwater(arr):
    left=1
    right=len(arr)-2
    lmax=arr[left-1]
    rmax=arr[right+1]
    res=0
    while left <= right :
        #if lmax is smaller,then we can decide water for arr[right]
        if rmax <= lmax :
            #added water of arr[right]
            res+=max(0,rmax-arr[right])
            #update rmax
            rmax=max(rmax,arr[right])
            #update right pointer 
            right-=1
        else:
            #add water for arr[left]
            res+=max(0,lmax-arr[left])
            #update lmax
            lmax=max(lmax,arr[left])
            #update left
            left += 1
    return res