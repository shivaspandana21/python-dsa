#Unique Code & Encoding
#Q1: Encoding
def encode_string(s):
    res, count = "", 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            res += s[i-1] + str(count)
            count = 1
    return res + s[-1] + str(count)

#Q2: Unique numeric code
def word_code(word):
    return "".join(str(ord(c) - 96) for c in word)