#15. Longest & Smallest Substring
#Q1: Longest word
def longest_word(sentence):
    return max(sentence.split(), key=len)

#Q2: Smallest substring containing all chars
def smallest_substring(s, t):
    from collections import Counter
    need, window = Counter(t), {}
    left = count = 0
    res = ""

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] <= need[ch]:
            count += 1
        while count == len(t):
            if not res or right - left + 1 < len(res):
                res = s[left:right+1]
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                count -= 1
            left += 1
    return res
