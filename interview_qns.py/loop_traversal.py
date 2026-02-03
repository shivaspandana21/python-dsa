"""A linguistic analysis tool needs to analyze sentences and count the number of vowels present 
to assess readability.
Test cases
• Input: "Artificial Intelligence" → Output: 10
• Input: "myths" → Output: 0"""
n=input()
vowels="aeiou"
count=0
for char in n:
    if char in vowels:
        count+=1
    else:
        count==0
print(count)

"""A debugging utility prints each character of a string on a separate line to help developers 
analyze character-level issues.Test cases
• Input: "debug"
• Input: "AI"""
n=input()
for i in range(len(n)):
    print(n[i])

