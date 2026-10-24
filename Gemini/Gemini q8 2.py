def find_pairs(numbers: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            # 较小的数放前面，利用集合自动去重
            pair = (complement, num) if complement < num else (num, complement)
            pairs.add(pair)
        seen.add(num)
        
    return sorted(list(pairs))

