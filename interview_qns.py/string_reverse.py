"""A debugging utility reverses strings without using built-in functions to test logical 
understanding.
Test cases
• Input: "hello" → "olleh"
• Input: "python" → "nohtyp"""


def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev 
"""A sentence processor reverses the order of words in a sentence.
Test cases
• Input: "learning is fun" → "fun is learning"
• Input: "code daily" → "daily code"""
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])