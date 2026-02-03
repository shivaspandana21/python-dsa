"""A username verification system checks whether a username is a palindrome to flag suspicious 
automated accounts.
Test cases
• Input: "madam" → True
• Input: "robot" → False"""
""" 
A system checks whether a word is a palindrome while ignoring case sensitivity.
Test cases
• Input: "Level" → True"""

"""l=[2,3,4,5,7,8]
rollno=5
for i in range(len(l)):
    if l[i]==rollno:
        print("index",i,"rollno",l[i])"""

arr=[17,50,12,9,5]
target=9
arr.sort()
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
else:
    print("NOT FOUND")
    

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