"""#day 1
#print max number in list
n=int(input())
a=list(map(int,input().split()))
max=0
for i in range(n+1):
    if a[i]>max:
        max=a[i]
print(max)
#or
n=int(input())
a=list(map(int,input().split()))
print(max(a))

#reverse right angle triangle
t=int(input())
n=int(input())
for i in range(n):
    for j in range(n):
        if j>=n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#or
#reverse right angle triangle
n=5
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#longest substring without vowels
t=int(input())
li=[]
for i in range(t):
    n=input()
    li.append(n)
for i in li:
    count=0
    max_count=0
    for char in i:
        if char not in "aeiou":
            count+=1
        else:
            count=0
max_count=max(max_count,count)
print(max_count)

#palindrome using two pointers
str=input()
i=0
j=len(str)-1
while i<j and str[i]==str[j]:
    i+=1
    j-=1
if i>=j:
    print("palindrome")
else:
    print("not palindrome")


#movie duration pair using two pointers
n=int(input())
duration=list(map(int,input().split()))
duration.sort()
target=int(input())
flag="No"
for i in range(n):
    for j in range(i+1,n):
        if duration[i]+duration[j]==target:
            flag="Yes"
            break
        if flag=="Yes":
            break
        print(flag)

#monotonous substring
#n queens
#sort using ascending order
#floyd's duplicate detection
#product of array except self"""
#peak element
arr=list(map(int,input().split()))
l=0
r=len(arr)-1
while l<r:
    mid=(l+r)//2
    if arr[mid]>arr[mid+1]:
        r=mid
    else:
        l=mid+1
print(l)
#max sub array
