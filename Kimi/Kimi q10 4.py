def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start = best_len = 0
    cur_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            cur_len = i - cur_start
            if cur_len > best_len:
                best_start, best_len = cur_start, cur_len
            cur_start = i

    if len(numbers) - cur_start > best_len:
        best_start, best_len = cur_start, len(numbers) - cur_start

    return numbers[best_start:best_start + best_len]
