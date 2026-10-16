def is_palindrome(s):
    """Return True if s reads the same forwards and backwards.

    The comparison is case-sensitive and includes spaces and punctuation
    (i.e. the string is compared exactly as given).
    """
    return s == s[::-1]
