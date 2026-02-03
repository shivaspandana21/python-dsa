"""A word-game application checks whether two words entered by players are anagrams of each 
other.
Test cases
• Input: "listen","silent" → True
• Input: "earth","heart" → True"""
def is_anagram(a, b):
    return sorted(a) == sorted(b)
"""
A language-learning application verifies whether two strings can be rearranged to form the 
same word.
Test cases
• Input: "study","dusty" → True
• Input: "note","tonee" → False"""
def is_anagram(a, b):
    return sorted(a) == sorted(b)