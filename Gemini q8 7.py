def find_pairs(numbers: list, target: int) -> list:
    seen_values = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen_values:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen_values.add(num)
        
    return sorted(list(pairs))

