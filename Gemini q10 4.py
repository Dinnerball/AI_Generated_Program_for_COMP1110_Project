def longest_increasing_run(numbers: list[int]) -> list[int]:
    if not numbers:
        return []
        
    max_start, max_len = 0, 1
    curr_start, curr_len = 0, 1
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
                max_start = curr_start
            curr_start = i
            curr_len = 1
            
    # 检查最后一轮循环
    if curr_len > max_len:
        max_len = curr_len
        max_start = curr_start
        
    return numbers[max_start:max_start + max_len]

