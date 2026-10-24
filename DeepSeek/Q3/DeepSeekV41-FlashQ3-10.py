def char_frequency(s):
    """Return a dictionary with the frequency of each character in s.

    Rules:
      * Every character is counted, including spaces.
      * Uppercase and lowercase letters are treated as different characters.
      * Nothing is printed; the result is returned.

    Example:
        >>> char_frequency("Hello World")
        {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
    """
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


if __name__ == "__main__":
    # Self-check only; the function itself never prints anything.
    assert char_frequency("") == {}
    assert char_frequency("aa") == {"a": 2}
    assert char_frequency("Aa") == {"A": 1, "a": 1}
    assert char_frequency("a b") == {"a": 1, " ": 1, "b": 1}
    assert char_frequency("Hello World") == {
        "H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "W": 1, "r": 1, "d": 1,
    }
    # Deliberately silent: running this file prints nothing.
