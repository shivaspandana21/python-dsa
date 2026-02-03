"""A digital dictionary compares two words entered by the user and determines which word 
should appear first alphabetically.
Test cases
• Input: "computer","science" → Output: "computer
n1=input()
n2=input()
s=ord(n1[0])
s1=ord(n2[0])
if s<s1:
    print(n1)
else:
    print(n2)

A school administration system sorts student names alphabetically for generating attendance 
sheets.
Test cases
• Input: ["Rahul","Anita","Suresh"] → ["Anita","Rahul","Suresh"]
• Input: ["Zara","Aman"] → ["Aman","Zara"]"""
n=input().split()
n.sort()
print(n)