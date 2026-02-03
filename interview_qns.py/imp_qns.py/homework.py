#Binary Tree Traversals
class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

#Build the class for tree operatrions
def build_tree(root,data):
  if root is None:
    return Node(data)
  if data<root.data:
    root.left=build_tree(root.left,data)
  else:
    root.right=build_tree(root.right,data)
  return root

#BFS traversal
def bfs(root):
  if root is None:
    return
  queue=[root]
  while queue:
    current=queue.pop(0)
    print(current.data,end=" ")
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)  

#DFS traversal
def pre_order(root):
  if root is None:
    return
  print(root.data,end=" ")
  pre_order(root.left)
  pre_order(root.right)

def in_order(root):
  if root is None:
    return
  in_order(root.left)
  print(root.data,end=" ")
  in_order(root.right)

def post_order(root):
  if root is None:
    return
  post_order(root.left)
  post_order(root.right)
  print(root.data,end=" ")

#Main code
values=list(map(int,input("Enter the element").split()))
root=None
for i in values:
  root=build_tree(root,i)
print("\nPreoreder Traversal-")
pre_order(root)
print("\nInoreder Traversal-")
in_order(root)
print("\nPostoreder Traversal-")
post_order(root)
print("\nLeveloreder(BFS) Traversal-")
bfs(root)


#Stack implementation of undo operation
stack =[]
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == "push":
        stack.append(s[1])
    elif s[0]=="undo":
        if len(stack)==0:
            print("No operation to undo")            
        else:
            stack.pop()            
print(*stack)

#Queue implementation
n = int(input())
queue = []
for i in range(n):
    s = input().split()
    if s[0] == "enqueue":
        queue.append(s[1])
    elif s[0]=="dequeue":
        if len(queue)==0:
            print("Queue is empty")            
        else:
            queue.pop(0)
print(*queue)

#Deque Occurrence Count
deque = [9,9,9]
v = int(input())
c=0
if len(deque)>0:
    for i in range(len(deque)):
        if deque[i] == v:
            c+=1    
print(c)



#Deque + Rotations                 
from collections import deque
# input
arr = list(map(int, input().split()))
d = deque(arr)
direction = input()    # "left" or "right"
k = int(input())
if len(d) == 0 or len(d) == 1:
    pass
else:
    if direction == "left":
        d.rotate(-k)
    elif direction == "right":
        d.rotate(k)
print(list(d))

#finding next greater element(monotonous stack)
def large_num(num):
  stack=[]#storing the index of the element which is not yet found
  result=[-1]*len(num)
  for i in range(len(num)):
    #while stack is not empty,AND current> existing
    while stack and num[i]>num[stack[-1]]:
      #pop the index at the top of stack
      index=stack.pop()
      #current is greater element,so print it in  result
      result[index]=num[i]
    stack.append(i)
  return result
print(large_num([4,5,2,25]))
print(large_num([13,7,6,12]))
print(large_num([5]))


#Floyds Cycle Detection
def duplicates(num):
    slow=num[0]
    fast=num[0]
#Detecting cycle
    while fast<len(num):
      if fast>=len(num) or num[fast]>=len(num):
         return "None"
      slow=num[slow]
      fast=num[num[fast]]
      if slow==fast:
        #then we have the cycle
        break
    slow=num[0]
    while slow!=fast:
       slow=num[slow]
       fast=num[fast]
    return slow
print(duplicates([1,3,4,2,2]))
print(duplicates([3,1,3,4,2]))
print(duplicates([1,1]))
#print(duplicates([1,2,3,4,5]))

#peak element
def peak(arr):
  left=0
  right=len(arr)-1
  while left<right:
    mid=(left+right)//2
    if arr[mid]>arr[mid+1]:#peak can lie on left
      right=mid
    else:
      left=mid+1 #peak lie on right
    #edge cases of 1st and last elements
  return left
print(peak([1,2,3,1]))
print(peak([10]))

#Trapping Rain Water
def trap_rainwater(arr):
  left=1
  right=len(arr)-2
  lmax=arr[left-1]
  rmax=arr[right+1]
  res=0
  while left<=right:
    #if lmax is smaller,then we can decide water for arr[right]
    if rmax<=lmax:
      #adding water of arr[right]
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
      left+=1
  return res
arr=[4,2,0,3,2,5]
print(trap_rainwater(arr))


#Movie duration problem(two pointer)
duration=[90,85,75,60,120,150]
target=180
flag=False
#step 1: sort the duration
duration.sort()
#step 2: initialize two pointers
i=0
j=len(duration)-1 #a.intialization
#step 3: iterate until pointers meet
if i<j:
  while i<j: #b.condition
    sum=duration[i]+duration[j]
    if sum==target:
      flag=True
      print(duration[i],duration[j])
      break
    elif sum<target:
      i+=1
    else:
      j-=1
    if flag==False:
      print("None")
elif len(duration)==1:
  if duration[0]==target:
    print(duration[0])
  else:
    print("None")
else:
    print("None")

#finding nth fibonacci number using recursion
def fibonacci(n):
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number:"))
print(fibonacci(n))

#find palindrome using recursion
def is_palindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome(s, start + 1, end - 1)     
s = input("Enter a string: ")
if is_palindrome(s, 0, len(s) - 1):
    print("palindrome")
else:
    print("not a palindrome")

#Print numbers in reverse using recursion
def reverse(i):
  if i==0:
    return
  print(i,end=" ")
  reverse(i-1)
i=int(input("Enter a number:"))
reverse(i)

#Binary search (Logistic problem)
def can_ship(weights,days,capacity):
  current_load=0
  used_days=1
  for i in weights:
    if current_load+i>capacity:
      used_days+=1
      current_load=0
    current_load+=i
  return used_days<=days
def min_ship_capacity(weights,days):
  min_cap=max(weights) #min capacity = max weight of 1 package
  max_cap=sum(weights) #max capacity sum of all package
  answer=max_cap
  while min_cap<max_cap:
    mid=(min_cap+max_cap)//2
    if can_ship(weights,days,mid):
      answer=mid
      max_cap=mid-1
    else:
      min_cap=mid+1
  return answer
print(min_ship_capacity([1,2,3,4,5,6,7,8,9,10],5))

#Sliding window
li=[27,13,50,45,9,37,24,91,57,20]
k=3
i=0
j=(i+(k-1))
res=sum(li[:k])
current=res
while(j<(len(li)-1)):
  i+=1
  j+=1
  current=current-li[i-1]
  current=current+li[j]
  if (res<current):
    res=current
print(res)

#permutations of a string using recursion
def permutations(arr):
    # Base case
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in permutations(remaining):
            result.append([current] + p)
    return result
print(permutations([1,2,3]))


#Array Rotation – Circular Data Handling
arr = [1,2,3,4,5]
k = 2
k = k % len(arr)
arr[:] = arr[-k:] + arr[:-k]
print(arr)

#Balanced Brackets Validation
s = "{[()]}"
stack = []
pairs = {')':'(', ']':'[', '}':'{'}
valid = True
for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()
if stack:
    valid = False
print(valid)

#Scientific Power Calculator (Fast Exponentiation)
x = 2
n = 10
res = 1
while n > 0:
    if n % 2 == 1:
        res *= x
    x *= x
    n //= 2
print(res)
#subsets with Target Sum – Backtracking Approach
def subsets_with_sum(nums, target):
    nums.sort()
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current.copy())
            return
        if remaining < 0:
            return

        for i in range(start, len(nums)):
            # skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current, remaining - nums[i])  # i+1 → no reuse
            current.pop()

    backtrack(0, [], target)
    return result

nums = [1,2,3,4,5]
target = 6
print(subsets_with_sum(nums, target))

#permutations
from itertools import permutations

def generate_permutations(input_list):
    result = []
    for p in permutations(input_list):
        result.append(list(p))
    return result

# Driver code
numbers =[1,2,3,4]
output = generate_permutations(numbers)

print(output)

