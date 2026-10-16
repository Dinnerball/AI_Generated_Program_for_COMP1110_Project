def char_frequency(s):
    """Return a dict mapping each character in s to its frequency.

    All characters are counted, including spaces. Uppercase and lowercase
    letters are treated as distinct characters.
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
