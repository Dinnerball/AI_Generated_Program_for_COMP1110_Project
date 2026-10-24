def char_frequency(s):
    """Return a dictionary mapping each character in s to its frequency.

    Every character is counted, including spaces. Uppercase and lowercase
    letters are treated as different characters. Nothing is printed.

    Example:
        char_frequency("Hello World")
        -> {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
    """
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
