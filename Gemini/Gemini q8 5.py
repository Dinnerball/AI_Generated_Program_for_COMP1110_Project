def find_pairs(numbers: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = (complement, num) if complement < num else (num, complement)
            pairs.add(pair)
        seen.add(num)
        
    return sorted(list(pairs))

