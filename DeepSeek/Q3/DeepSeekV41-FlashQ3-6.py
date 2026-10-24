"""
COMP1110 Q3 - Character frequency counter.

char_frequency(s) returns a dictionary mapping each character in s to the
number of times it occurs. All characters are counted, including spaces,
and uppercase/lowercase letters are treated as distinct characters.
Nothing is printed.
"""


def char_frequency(s):
    """Return a dict of character -> occurrence count for the string s.

    Every character is counted, including spaces and punctuation, and
    letters are case sensitive ('A' and 'a' are different keys).

    Args:
        s: The string to inspect.

    Returns:
        A dictionary whose keys are the characters found in s and whose
        values are their frequencies.
    """
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


if __name__ == "__main__":
    # Individual tests; results are only shown here, the function itself
    # never prints anything.
    assert char_frequency("") == {}
    assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert char_frequency("a A") == {"a": 1, " ": 1, "A": 1}
    assert char_frequency("aaAA") == {"a": 2, "A": 2}
    assert char_frequency("  ") == {" ": 2}
    result = char_frequency("Hello World")
    print(result)
