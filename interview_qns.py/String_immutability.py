"""A document editor needs to replace a character at a specific position while keeping the 
original text unchanged.
Design a logic using slicing to achieve this."""
n=input()
index=int(input())
new_char=input()
r=n[:index]+new_char+n[index+1:]
print(r)

"""A cybersecurity system attempts to update a password character directly for masking 
purposes but fails during execution.
Explain why strings cannot be modified directly and demonstrate how to create a modified 
version of the string instead.
Test cases
• Input: "secure123" → Attempt direct modification → Error
• Input: "welcome" → Attempt direct modification → Error"""
n=input()
n[5]="P"
print(n)#TypeError: 'str' object does not support item assignment