def second_largest(nums):
    first = second = float('-inf')
    for x in nums:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return second