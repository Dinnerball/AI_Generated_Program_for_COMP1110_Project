def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start = 0
    best_length = 1

    run_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            run_length = i - run_start

            if run_length > best_length:
                best_length = run_length
                best_start = run_start

            run_start = i

    run_length = len(numbers) - run_start
    if run_length > best_length:
        best_length = run_length
        best_start = run_start

    return numbers[best_start:best_start + best_length]
