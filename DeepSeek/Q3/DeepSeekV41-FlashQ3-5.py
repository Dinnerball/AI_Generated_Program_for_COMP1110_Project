def char_frequency(s):
    """Return a dictionary mapping each character in s to its frequency.

    Every character is counted, including spaces. Uppercase and lowercase
    letters are treated as distinct characters.
    """
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
