def char_frequency(s: str) -> dict[str, int]:
    """Returns a dictionary containing the frequency of each character in a string."""
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

