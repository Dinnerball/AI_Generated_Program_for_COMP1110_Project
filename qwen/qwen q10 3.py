def two_sum(nums, target):
    nums_sorted = sorted((x, i) for i, x in enumerate(nums))
    left, right = 0, len(nums_sorted) - 1
    while left < right:
        s = nums_sorted[left][0] + nums_sorted[right][0]
        if s == target:
            return sorted([nums_sorted[left][1], nums_sorted[right][1]])
        elif s < target:
            left += 1
        else:
            right -= 1