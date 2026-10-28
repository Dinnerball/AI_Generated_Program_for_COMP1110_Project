def find_missing(nums):
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)