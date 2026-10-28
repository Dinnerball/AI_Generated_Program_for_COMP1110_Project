def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return sorted([seen[target - x], i])
        seen[x] = i