def find_missing(nums):
    missing = 0
    for x in nums:
        missing ^= x
    for x in range(1, len(nums) + 2):
        missing ^= x
    return missing