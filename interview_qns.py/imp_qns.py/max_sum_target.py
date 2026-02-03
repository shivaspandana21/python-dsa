def subsets_with_sum(nums, target):
    nums.sort()
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current.copy())
            return
        if remaining < 0:
            return

        for i in range(start, len(nums)):
            # skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current, remaining - nums[i])  # i+1 → no reuse
            current.pop()

    backtrack(0, [], target)
    return result

nums = [1,2,3,4,5]
target = 6
print(subsets_with_sum(nums, target))
