"""
a warehouse handles packages of 3 diff priority level during dispatch 0 is for low priority 1 medium 2 high all package arrive on
        in random order befor dispatch the warehoue must rearrange the packages aso that all low priority come fst followed by medium and high priority you are given list of integers where each integer  is either 1 2 0 rearrange the list so that all 0 appear first then 1 and then 2 
rules:
do not use bulit in fun
do not use extra list
modify the list in place
"""

#recurssion
"""
fun calling itself
process b iterate a selective statements oining to perform the specific task"->repetion->loops-> 1)initialize 2)condition 3)update

i=1
def recursive(i):
    if i<=10:
        print(i)
        i+=1
        recursive(i)
    return
def start():
    user=input("write start to begin")
    if user=='start':
        recursive(i)
    print("end of recurive")
start()

def recursive(i,user):
    if i<=10:
        print(user*i)
        i+=1
        recursive(i,user)
    return
def start():
    user=int(input("enter n value"))
    recursive(1,user)
    print("end of recurive")
start()

def recursive(i,user):
    if i<=10:
        print(user*i)
        i+=1
        recursive(i,user)
    return
def start():
    user=int(input("enter n value"))
    recursive(1,user)
    print("end of recurive")
start()"""

# reverse counting from n to 1
# sum of list
# sum of n natural numbers
# fibonacci
# factorial
# string palindrome\

def list_sum(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
        
    return sum
l=list(map(int,input().split()))
print(list_sum(l))  


# reverse counting from n to 1
def n_to_1(n):
    if n == 0:
        return
    else:
        print(n,end=" ")
        n_to_1(n-1)
n_to_1(10)

# sum of list

def sum_of_L(li,ind):
    if ind == len(li):
        return 0
    sum_li =li[ind] + sum_of_L(li,ind+1)
    return sum_li

print(sum_of_L([1,2,3,4,5],0))

# sum of n natural numbers
def sum_of_n(n):
    if n == 0:
        return 0
    summation = n + sum_of_n(n-1)
    return summation

print(sum_of_n(10))

# fibonacci
def fibonacci(first,second,n):
    if n == 2:
        return
    next = first + second
    n-=1
    print(next,end=" ")
    fibonacci(second,next,n)

first = 0
second = 1
print(first,second,end=" ")
(fibonacci(0,1,5))

# factorial
def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))

print(factorial(5))

# string palindrome
def palindrome(start,end,s):
    if start>end:
        return True
    return s[start] == s[end] and palindrome(start+1,end-1,s)

s = "malayalam"
print(palindrome(0,len(s)-1,s))

# A warehouse handles packages of 3 different priority levels during dispatch     0-> low , 1-> medium, 2-> high
# All packages arrive on a conveyor belt in random order , before dispatch the warehouse system must re-arrange the 
# packages so that all low priority packages come first followed by medium and then high priority packages.you're
#  given a list of integers , where each integer is either 0 or 1 or 2    re-arrange the list in-place so that all 
# zeros appear first , then one's then two's
# do not use built-in sort function , extra array space and only modify the list in-place

# for every recursive function to start you need to call it at least one time explicitly

'''
We get RecursionError if it gets to infinite loop and not having a base case.
because we have limited space in the RAM.
'''

i=1
def recursive(i):
    if i<=10:
        print(i)
        i+=1
        recursive(i)
    return
def start():
    user=input("write start to begin")
    if user=='start':
        recursive(i)
    print("end of recurive")
start()

# reverse counting from n to 1
def n_to_1(n):
    if n == 0:
        return
    else:
        print(n,end=" ")
        n_to_1(n-1)
n_to_1(10)

# sum of list

def sum_of_L(li,ind):
    if ind == len(li):
        return 0
    sum_li =li[ind] + sum_of_L(li,ind+1)
    return sum_li

print(sum_of_L([1,2,3,4,5],0))

# sum of n natural numbers
def sum_of_n(n):
    if n == 0:
        return 0
    summation = n + sum_of_n(n-1)
    return summation

print(sum_of_n(10))

# fibonacci
def fibonacci(first,second,n):
    if n == 2:
        return
    next = first + second
    n-=1
    print(next,end=" ")
    fibonacci(second,next,n)

first = 0
second = 1
print(first,second,end=" ")
(fibonacci(0,1,5))

# factorial
def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))

print(factorial(5))

# string palindrome
def palindrome(start,end,s):
    if start>end:
        return True
    return s[start] == s[end] and palindrome(start+1,end-1,s)

s = "malayalam"
print(palindrome(0,len(s)-1,s))

def quick_sort(arr):
    if len(arr) <= 1:   
        return arr
    pivot = arr[0]     
    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([5, 3, 8, 4, 2]))
print(quick_sort([5,9,8,3,6,2,1]))

#recursion -> func calling itself | repetition
# repition -> Loops - 1) initialize 2)condition 3)update
def calc(i):       
    if i > 5:      # base case
        return
    print("good day")
    i+=1
    calc(i)
    print()
    print(i)

calc(1)