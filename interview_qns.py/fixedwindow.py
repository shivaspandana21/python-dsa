#Fixed & Variable Window
#Q1: Fixed window max sum
def max_sum_subarray(arr, k):
    curr = max_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        curr += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr)
    return max_sum

#Q2: Longest unique substring
def longest_unique_substring(s):
    seen = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
