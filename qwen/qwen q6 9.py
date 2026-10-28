def find_missing(nums):
    n = len(nums) + 1
    return (set(range(1, n + 1)) - set(nums)).pop()