def longest_increasing_run(numbers):
    if not numbers:
        return []

    longest = [numbers[0]]
    current = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current.append(numbers[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [numbers[i]]

    if len(current) > len(longest):
        longest = current

    return longest