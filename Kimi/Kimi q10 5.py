def longest_increasing_run(numbers):
    if not numbers:
        return []

    best_start = best_end = 0  # indices, inclusive
    run_start = 0

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            # run [run_start, i-1] ended
            if i - 1 - run_start > best_end - best_start:
                best_start, best_end = run_start, i - 1
            run_start = i

    # check the final run
    if len(numbers) - 1 - run_start > best_end - best_start:
        best_start, best_end = run_start, len(numbers) - 1

    return numbers[best_start:best_end + 1]
