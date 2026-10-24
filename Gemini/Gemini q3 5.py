def char_frequency(s: str) -> dict[str, int]:
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

