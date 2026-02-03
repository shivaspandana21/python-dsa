n=5
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1, 4):
    # print spaces
    for s in range(3 - i):
        print(" ", end="")

    # print stars with space
    for j in range(1, i + 1):
        print("*", end=" ")
    
    print()



n = 6

for i in range(n):
    print(" " * i, end="")

    # first row: full stars
    if i == 0:
        print("*" * (2*n - 1))
    # last row: single star
    elif i == n - 1:
        print("*")
    else:
        # hollow middle rows
        inner_spaces = 2*(n - i) - 3
        print("*" + " " * inner_spaces + "*")
   

n=3   
for i in range(n):
    for j in range(2*n-1):
        if i+j==2 or j-i==2:
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(2*n-1):
        if j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(2*n-1):
        if i-j==0 or i+j==4:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print() 


#or
n=5
for i in range(n):
    for j in range(2*n-1):
        if j==(n-1-i) or j==(n-1+i):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()

# hallow square
for i in range(n):
    for j in range(2*n-1):
        if j==0 or j==2*n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# inverted hallow triangle not right angled
for i in range(n):
    for j in range(2*n-1):
        if j==i or j==(2*n-2-i):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()

n=3
for i in range(n):
    for j in range(n):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if j>=(n-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#left diagonal and right diagonal side by side
n=3
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if j==(n-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    #perfect square
    n=5 
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

   

n=int(input("enter n: "))
for i in range(1,n+1):
    if i%4==0 or i%10==7:
        print(i,end=" ")

year=int(input("enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year") 

# given a list of 7 integer num placed randomly find all the pairs if the list numbers whose sum is equal to user input n if there is  no pair found return none
n=int(input("enter n: "))
l=[10,15,3,7,8,5,2]
sum=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==n:
            print("pair is:",(l[i],l[j]))
        else:
            print("none")       

#to print amstrong number between 1 to n
n=int(input("enter n: "))
for num in range(1,n+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if sum==num:
        print(num,"is amstrong number")
#or
def is_amstrong(num):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    return sum==num
amstrong_numbers = []
for i in range(1, 1001):
    if is_amstrong(i):
        amstrong_numbers.append(i)      
print("Amstrong numbers between 1 and 1000:", amstrong_numbers)


#to check whether a number is amstrong or not
n=int(input("enter n: "))
temp=n
sum=0
n_digits=len(str(n))
while temp>0:
    rem=temp%10
    sum+=rem**n_digits
    temp//=10
if sum==n:
    print(n,"is amstrong number")
else:
    print(n,"is not amstrong number")


#or
n=int(input("enter n: "))
for num in range(1,n+1):
    digits=str(num)
    power=len(digits)
    #calculate amstrong
    arm_sum=0
    for d in digits:
        arm_sum+=int(d)**power
#matching the condition
    if arm_sum==num:
        print(num,"is amstrong number")
    else:
        print(num,"is not amstrong number")

# given 20 random num which can be repeated also write a python code to print top kth frequent num in the list
l=[1,2,3,4,5,1,2,3,1,2,1,6,7,8,9,6,5,4,3,2]
k=int(input("enter k: "))
count=0
temp=[]
for i in l:
    if i not in temp:
        freq=l.count(i)
        temp.append((i,freq))



#or
l=[1,2,3,4,5,1,2,3,1,2,1,6,7,8,9,6,5,4,3,2]
count=0
temp=0
for x in l:
    if x==l:
        count+=1
        if count>=temp:
            temp=count
    else:
        count=0
print("top k frequent num is:",temp)

l=list(map(int,input("enter list elements: ").split()))
n=int(input("enter n: "))
count=0
for i in l:
    if i==n:
        count+=1    
print(n,"occurs",count,"times in the list")
#now print top k frequent num
freq_dict={}    
for i in l:
    if i in freq_dict:
        freq_dict[i]+=1
    else:
        freq_dict[i]=1
sorted_freq=sorted(freq_dict.items(),key=lambda x:x[1],reverse=True)#triggers the sorting based on frequency in descending order 
k=int(input("enter k: "))   
print("top",k,"frequent numbers are:")
for i in range(k):
    print(sorted_freq[i][0],"with frequency",sorted_freq[i][1]) 