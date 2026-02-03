"""#using functions
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=int(input())
result=fact(x)
print(result)

#normal 
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)

#using recurssion
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1) 
print(fact(5))

#clumsy factorial
def clumsy(n):
    k=0
    stack=[n]
    for i in range(n-1,0,-1):
        if k%4==0:
            stack.append(stack.pop()*i)
        elif k%4==1:
            stack.append(int(stack.pop()/i))    
        elif k%4==2:
            stack.append(i)
        else:
            stack.append(-i)
        k+=1
    return sum(stack)
n = int(input())
print(clumsy(n))"""

#check whether the num fact is palindrome or not
n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)
rev=0
temp=f
while f>0:
    d=f%10
    rev=rev*10+d
    f=f//10
if rev==temp:
    print("given fact is palindrome")
else:
    print("not palindrome")
#trailing zero
def trailing_zero(n):
    count=0
    i=5
    while i<=n:
        count+=n//i
        i*=5
    return count
n=int(input())
print(trailing_zero(n))

#check whether the num fact is palindrome or not
f=int(input())
temp=f
rev=0
while f>0:
    d=f%10
    rev=rev*10+d
    f=f//10
if temp<2:
    print("not prime palindrome")
else:
    for i in range(2, temp):
        if temp % i == 0:
            print("not prime palindrome")
            break
    else:
        if temp==rev:
            print("prime palindrome")
        else:
            print("Not prime palindrome")
        