"""A password validation system checks whether a password contains duplicate characters, 
which may weaken security.
Test cases
• Input: "secure" → No duplicates
• Input: "password" → Duplicate detected"""

def has_duplicates(s):
    len(set(s)) != len(s)
    return"No duplicates"


n=input()
print(has_duplicates(n))
"""
A data-cleaning tool removes duplicate characters from user input while preserving the 
original order.
Test cases
• Input: "banana" → "ban"
• Input: "engineering" → "enginr"""

def remove_duplicates(s):
    result = ""
    for ch in s:
        if ch not in result:
            result += ch
    return result
print(remove_duplicates(n))