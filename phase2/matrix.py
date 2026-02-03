"""nums=list(map(int,input().split()))
d=[]
for i in range(len(nums)):
    if nums[i] in d:
        print("false")
        break
    d.append(nums[i])
else:
    print("true")"""

"""def find_duplicate(nums):
    d=[]
    for i in range(len(nums)):
        if nums[i] in d:
            return ("false")
        d.append(nums[i])
    else:
        return("true")
nums=list(map(int,input().split()))
print(find_duplicate(nums))

#neetcode contain duplicate
class Solution:
    def hasDuplicate(self, nums):
        d=[]
        for i in range(len(nums)):
            if nums[i] in d:
                return True
                break
            d.append(nums[i])
        else:
            return False"""
"""#two sum
nums=list(map(int,input().split()))
target=int(input())
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])
#or
class Solution:
    def twoSum(self, n, k):
        i = 0
        j=len(n)-1
        while i<j:
            if n[i]+n[j]==k:
                return i,j
                break
            else:
                j-=1
                if j==i:
                    i+=1
                    j=len(n)-1
#or
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]],i]   
            else:
                d[nums[i]]=i"""

nums = list(map(int, input().split()))
target = int(input())
d = {}

for i in range(len(nums)):
    if target - nums[i] in d:
        print([d[target - nums[i]], i])
        break
    else:
        d[nums[i]] = i









        
