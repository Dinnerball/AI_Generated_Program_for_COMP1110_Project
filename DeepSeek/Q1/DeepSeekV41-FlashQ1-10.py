def is_palindrome(s):
    """Return True if s reads the same forwards and backwards.

    The comparison is case-sensitive and includes spaces and punctuation.
    No output is printed; a Boolean value is returned.
    """
    return s == s[::-1]
