"""
A streaming platform wants to suggest two movies to the user, such that there total watch time is exactly equals to the available free time the user has. 
You're given a list of movie durations in minutes and a target time 't'.
Write a function that finds one pair of movie durations whose time is exactly 't'.
# Constraints : Each movie can be used only once. return the pair of durations.
# if no pair exists return none
test case 1 :
duration = [90,85,75,60,120,150]
target = 180
output = [60,120]

test case 2 :
duration = [40,50,60,70]
target = 90
output = [40,50]

test case 3 :
duration = [100]
target = 110
output = NONE"""


def pair_movies(durations, target):
    sorted_durations = sorted(durations)
    for i in range(len(sorted_durations)):
        for j in range(i+1, len(sorted_durations)):
            if sorted_durations[i] + sorted_durations[j] == target:
                return [sorted_durations[i], sorted_durations[j]]
    return None
duration=[90,85,75,60,120,150]
target=180
print(pair_movies(duration,target))

#or 
duration=[40,50,60,70]
#step 1 sorting
duration.sort()
target=90
i,j=0,len(duration)-1 #intializing two pointers
sum=duration[i]+duration[j]
#step 3 end the case
while(i<j):
    #step 2 match and update pointers 
    if sum==target:
        print(duration[i],duration[j])
    elif sum<target:
        i+=1
    else:
        j-=1
else:
    if len(duration)==1 and duration[0]==target:
        print(duration[0])
    else:
        print("NONE")




arr=[2,23,50,45,9,37,24,91,57,20]
k=3
i=0
j=i+k-1

max_sum=0
while(j<=len(arr)-1):
    sum=sum(arr[i:j+1])
    max_sum=max(max_sum,sum)
    i+=1
    j+=1
print(max_sum)

"""


Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""
 
def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
n=int(input())
print(fizzBuzz(n))

class Solution:
    def fizzBuzz(self,n):
        result=[]
        for i in range(n+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
n = int(input())
obj = Solution()
a = obj.fizzBuzz(n)
print(a)
        
        