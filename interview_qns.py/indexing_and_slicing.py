'''An online learning platform stores student email IDs in a database.
For generating student usernames, the system must extract the part of the email before the 
‘@’ symbol using string indexing and slicing.
Design a program to perform this operation.
Test cases
• Input: "student2024@university.edu" → Output: "student2024"
• Input: "admin@portal.com" → Output: "admin"'''
s=input()
at_index=s.index('@')
print(s[:at_index])

"""A warehouse management system uses alphanumeric product codes where the last four 
characters represent the product category.
The system must extract this category code for inventory classification.
Test cases
• Input: "PRD7834ELEC" → Output: "ELEC"
• Input: "ITEM9945FOOD" → Output: "FOOD"""
n=input()
print(n[-4:])


