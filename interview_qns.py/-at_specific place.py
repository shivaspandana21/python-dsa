"""A text-editing tool removes a character at a given index as specified by the user.
Test cases
• Input: "hello", index=1 → "hllo"
• Input: "world", index=2 → "wold"""

def remove_at_index(s, index):
    return s[:index] + s[index+1:]
"""
A string processor removes the middle character of a word for formatting purposes.
Test cases
• Input: "abcde" → "abde"
• Input: "training" → "trainng"
"""
def remove_middle(s):
    mid = len(s) // 2
    return s[:mid] + s[mid+1:]