#list of poistive integers and a num k find the length of the longest subarray whose sum is less than or equal to k using sliding window technique
#input:l=[2,1,5,1,3,2],k=7
#output:3
l=[2,1,5,1,3,2]
sub_array=[]
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        sub_array.append(l[i:j])
print(sub_array)
data=[2,1,5,1,3,2]
k=7
rlen=0
result=[]
n=len(data)
for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum +=data[j]
        if(sum<=k):
            result.append(data[j])
        else:
            result.clear()
            sum=0
    if(rlen<len(result)):
        rlen=len(result)
        print(result)
    result.clear()
print(rlen)


data=[2,1,5,1,3,2]
k=7
result=[]
n=len(data)
for i in range(n):
    sum=0
    d1=[]
    for j in range(i,n):
        sum +=data[j]
        if(sum<=k):
            d1.append(data[j])
    result.append(d1)
max_len=0   
for i in result:
    if(len(i)>max_len):
        max_len=len(i)
        print(i)
print(max_len)


"""is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.""" 
from collections import Counter
n=int(input())
sizes=list(map(int,input().split()))
size_count=Counter(sizes)
m=int(input())
earnings=0  
for i in range(m):
    size,price=map(int,input().split())
    if size_count[size]>0:
        earnings +=price
        size_count[size]-=1
print(earnings)

s=5
y=lambda x:x*x
print(y(s))

def learn(n):
    return lambda x:x+n
add5=learn(5)
print(add5(10))

#reverse right angle triangle
n=5
for i in range(n):
    for j in range(n):
        if j>=n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

