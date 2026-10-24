def is_palindrome(s):
    """Return True if s reads the same forwards and backwards, else False.

    The comparison is case-sensitive and treats spaces and punctuation as
    ordinary characters.
    """
    return s == s[::-1]
