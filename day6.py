"""Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate
Docstring for day6"""


arr=[1,1,1,1,1]
d=3
m=2
a=[]
for i in range(len(arr)+1):
    for j in range(i+1,len(arr)+1):
        if sum(arr[i:j])==d and len(arr[i:j])==m:
            a.append(arr[i:j])
print(len(a))
#or
def birthday(arr,d,m):
    a=[]
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            if sum(arr[i:j])==d and len(arr[i:j])==m:
                a.append(arr[i:j])
    return len(a)
n=int(input())
arr=list(map(int,input().split()))  
d,m=map(int,input().split())
print(birthday(arr,d,m))


def birthday(s, d, m):
    a=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if sum(s[i:j])==d and len(s[i:j])==m:
                a+=1
    return a
n=int(input())
s=list(map(int,input().split()))
d,m=map(int,input().split())
print(birthday(s,d,m))


s=input()
p=input()
for i in range(len(s)-len(p)+1):
    match=True
    for j in range(len(p)):
        if s[i+j]!=p[j]:
            match=False
            break
    if match:
        print(True)

#or
"""1.find s & p
   2.count p into hash
   3.for length of p find hash of sth subarray in s
   4.start iteration & do comparison of both hash
   5.follow sliding window technique
   6.if both hash get matched check the sequence of string
   7.if mathed end else continue the len(s)-len(p)

#find substring of s of length 3"""

s=input()
k=3
for i in range(len(s)-k+1):
    print(s[i:i+k])
#find substring of s of length 3 which consists of max no of vowels among all possible substrings
s=input()
k=3
vowels="aeiou"
max_vowel_count=0
result_substring=""
for i in range(len(s)-k+1):
    substring=s[i:i+k]
    print(substring)
    vowel_count=0
    for char in substring:
        if char in vowels:
            vowel_count+=1
    if vowel_count>max_vowel_count:
        max_vowel_count=vowel_count
        result_substring=substring
print(result_substring)



def rabin_karp(s,p):
    n=len(s)
    m=len(p)

    if m==0:
        return True
    if m>n:
        return False
    
    base=26
    mod=10000000007
    pattern_hash=0
    window_hash=0
    power=1   #base^(m-1)


    #computing the base
    for _ in range(m-1):
        power=(power*base)%mod

    #compute the pattern of 1st window
    for i in range(m):
        pattern_hash=(pattern_hash*base+ord(p[i]))%mod

        window_hash=(window_hash*base+ord(s[i]))%mod

    #slide the window
    for i in range(n-m+1):

        #if hashes match, verify the char sequence
        if pattern_hash==window_hash:
            match=True
            for j in range(m):
                if s[i+j]!=p[j]:
                    match=False
                    break
            if match:
                return True
        if i<n-m:
            #remove the left character
            window_hash=(window_hash-ord(s[i])*power)%mod

            #adding right character
            window_hash=(window_hash*base+ord(s[i+m]))%mod

            window_hash=(window_hash+mod)%mod #ensuring +ive hash

    return False

print(rabin_karp("abcabd","cab"))

s=input()
target=input()
index=0
for i in range(len(s)):
    if s[i]==target[index]:
        index+=1
    if index==len(target):
        print(True)
        break
else:
        print(False)


#or
def hackerrankInString(s):
    target="hackerrank"
    index=0
    for i in range(len(s)):
        if s[i]==target[index]:
            index+=1
        if index==len(target):
            return "YES"
    return "NO" 
        
s1=input()
s2=input()
count=0
for char in s1:
    if char in s2:
        count+=1
    if count==1:
        print("YES")
        break
else:
    print("NO")

"""Check whether ,  and  are divisors of . All 3 numbers divide evenly into  so return ."""
d=int(input())

n=list(map(int,str(d)))
count=0
for i in range(len(n)):
    if d%n[i]==0:
        count+=1
print(count)

def findDigits(n):
    count=0
    for char in str(n):
        digit=int(char)
        if digit!=0 and n%digit==0:
            count+=1
    return count
    
      