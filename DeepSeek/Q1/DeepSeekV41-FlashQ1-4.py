def is_palindrome(s):
    """Return True if s reads the same forwards and backwards.

    The comparison is case-sensitive and takes spaces and punctuation
    into account, so no normalisation is performed on the input.
    """
    return s == s[::-1]
