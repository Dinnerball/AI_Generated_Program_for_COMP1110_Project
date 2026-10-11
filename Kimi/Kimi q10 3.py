def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start = 0
    best_len = 1
    curr_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            continue  # run still growing
        curr_len = i - curr_start
        if curr_len > best_len:
            best_start = curr_start
            best_len = curr_len
        curr_start = i

    # check the final run
    curr_len = len(numbers) - curr_start
    if curr_len > best_len:
        best_start = curr_start
        best_len = curr_len

    return numbers[best_start:best_start + best_len]
