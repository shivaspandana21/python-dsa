"""A plagiarism checker scans documents to detect whether a particular keyword appears within 
a large paragraph.
Test cases
• Input: "learning python programming","python" → True
• Input: "data science","java" → False"""
"""s1=input()
s2=input()
if s2 in s1:
    print("True")
else:
    print("False")"""
"""A text-analysis system counts how many times a particular substring occurs within a 
sentence.
Test cases
• Input: "abababa","aba" → 2
• Input: "aaaaa","aa" → 4"""
s1 = input()
s2 = input()

count = s1.count(s2)
print(count)
#or
s1 = input()
s2 = input()
n=len(s1)
n1=len(s2)
count = 0
i=0
while i<=n-n1:
    if s1[i:i+n1]==s2:
        count+=1
        i+=n1 #skip overlapping part
    else:
        i+=1
print(count)

def substring(s):
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            print(s[i:j])
                
s='abc'
print(substring(s))


def substring(s1,s2):
    m=len(s1)
    n=len(s2)
    for i in range(m-n+1):
        j=0
        while j<n and s1[i+j]==s2[j]:
            j+=1
        if(j==n):
            return i
    return -1

s1=input("enter s1 string:")
s2=input("enter s2 string:")
result=substring(s1,s2)
if (result!=-1):
    print("index found at",result)
else:
    print("not found")

def substring(s):
    n=len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            print(s[i:j])
s=input("enter s string:")
print(substring(s))

def longest_substring(s):
    s1=set()
    left=0
    max_len=0
    for right in range(len(s)):
        while s[right] in s1:
            s1.remove(s[left])
            left+=1
        s1.add(s[right])
        max_len=max(max_len,right-left+1)
    return max_len 

s=input("enter s string:")
print(longest_substring(s))