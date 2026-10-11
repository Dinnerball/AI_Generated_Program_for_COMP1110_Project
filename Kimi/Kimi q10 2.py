def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start, best_len = 0, 1
    cur_start, cur_len = 0, 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            cur_len += 1
        else:
            cur_start, cur_len = i, 1
        if cur_len > best_len:  # strict > keeps the earliest on ties
            best_start, best_len = cur_start, cur_len

    return numbers[best_start:best_start + best_len]
