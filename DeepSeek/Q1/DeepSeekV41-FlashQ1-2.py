def is_palindrome(s):
    """Return True if s reads the same forwards and backwards.

    The comparison is case-sensitive and counts every character,
    including spaces and punctuation. Returns a Boolean value and
    prints nothing.
    """
    return s == s[::-1]
