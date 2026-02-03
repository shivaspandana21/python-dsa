def max_sum_subarray(arr, k):
    window_sum = 0                 # stores sum of current window
    max_sum = float('-inf')        # stores maximum sum found

    # Step 1: Calculate sum of first window (first k elements)
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum           # initialize max_sum

    # Step 2: Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i]       # add new element to window
        window_sum -= arr[i - k]   # remove element going out of window

        # update maximum sum
        max_sum = max(max_sum, window_sum)

    return max_sum
arr=[2,4,9,8,5,6,8,9]
k=3
print("Maximum sum of a subarray of size", k, "is:", max_sum_subarray(arr, k))