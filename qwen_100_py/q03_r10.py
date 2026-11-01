def char_frequency(s):
    frequencies = {}
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies
