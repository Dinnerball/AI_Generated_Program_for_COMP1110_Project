def find_pairs(numbers: list, target: int) -> list:
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)
        
    return sorted(list(pairs))

