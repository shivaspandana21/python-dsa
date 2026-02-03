"""A chatbot analyzes messages to determine how frequently each character appears for 
sentiment analysis.
Test cases
• Input: "hello" → {h:1,e:1,l:2,o:1}
• Input: "chatbot" → {c:1,h:1,a:1,t:2,b:1,o:1}"""
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

"""
A text analyzer finds the most frequently occurring character in a paragraph.
Test cases
• Input: "success" → s
• Input: "analytics" → a"""
def most_frequent_char(s):
    freq = char_frequency(s)
    return max(freq, key=freq.get)