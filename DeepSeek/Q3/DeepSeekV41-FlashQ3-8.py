def char_frequency(s):
    """Return a dictionary mapping each character in s to the number of times it appears.

    All characters are counted, including spaces. Uppercase and lowercase
    letters are treated as different characters. Nothing is printed.

    Args:
        s: The string to analyze.

    Returns:
        A dict where each key is a character from s and each value is its count.
    """
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
