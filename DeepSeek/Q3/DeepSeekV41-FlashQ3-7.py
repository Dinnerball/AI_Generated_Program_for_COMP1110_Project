"""COMP1110 Q3 - character frequency counter.

char_frequency(s) returns a dict mapping each character in s to the number of
times it occurs. Spaces are counted, and uppercase/lowercase letters are
treated as distinct characters (no case folding). Nothing is printed.
"""


def char_frequency(s):
    """Return {character: count} for every character in the string s.

    Every character is counted, including spaces. 'A' and 'a' are different
    keys. The function returns the dictionary and prints nothing.

    >>> char_frequency("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    >>> char_frequency("Aa a")
    {'A': 1, 'a': 2, ' ': 1}
    >>> char_frequency("")
    {}
    """
    frequencies = {}
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies
