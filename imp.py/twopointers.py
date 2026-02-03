"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""
"""#two sum
arr = [3, 2, 4]
k = 6
arr.sort()
i = 0
j = len(arr) - 1

while i < j:
    if arr[i] + arr[j] == k:
        print(i, j)   # indices
        
    elif arr[i] + arr[j] > k:
        j -= 1
    else:
        i += 1
#or
arr = [3,3]
k = 6

i = 0
j = len(arr) - 1

while i < j:
    if arr[i] + arr[j] == k:
        print(i, j)
        break
    else:
        j -= 1
        if j == i:
            i += 1
            j = len(arr) - 1

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
# sub array sum
arr=[1,2,3]
k=3
count=0
i=j=current_sum=0
while j<len(arr):
    current_sum+=arr[j]
    while current_sum>k:
        current_sum-=arr[i]
        i+=1
    if current_sum==k:
        count+=1
        
    j+=1
print(count)


#merge sorted array 
a1=[3,9,27,42]
a2=[19,23,39,56]
a3=[]
i=0
j=0
while i<len(a1) and j<len(a2):
        
        if a1[i]<a2[j]:
            a3.append(a1[i])
            i+=1
        else:
            a3.append(a2[j])
            j+=1
print(a3)
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
def move_zeros(n):
    j=0

    for i in range(len(n)):
        if n[i]!=0:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
            j+=1
    return n
n=[3,1,0,3,1,1]
print(move_zeros(n))"""

#max sum of subarray
arr=[27,13,50,45,9,37,24,91,57,20]
k=3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum+=arr[i]
    window_sum-=arr[i-k]
    max_sum=max(window_sum,max_sum)
print(max_sum)
