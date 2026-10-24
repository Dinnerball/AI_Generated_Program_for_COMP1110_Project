def find_pairs(numbers: list[int], target: int) -> list[tuple[int, int]]:
    """Returns a sorted list of unique pairs that sum up to the target."""
    seen = set()
    pairs = set()
    
    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)
        
    return sorted(list(pairs))

