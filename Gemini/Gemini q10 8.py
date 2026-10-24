def longest_increasing_run(numbers: list) -> list:
    if not numbers:
        return []
        
    max_start, max_len = 0, 1
    current_start, current_len = 0, 1
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
            current_start = i
            current_len = 1
            
    if current_len > max_len:
        max_len = current_len
        max_start = current_start
        
    return numbers[max_start:max_start + max_len]

