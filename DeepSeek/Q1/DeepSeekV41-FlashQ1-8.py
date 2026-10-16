def is_palindrome(s):
    """Return True if s reads the same forwards and backwards.

    The comparison is case-sensitive and keeps every character,
    including spaces and punctuation.
    """
    return s == s[::-1]


if __name__ == "__main__":
    assert is_palindrome("racecar") is True
    assert is_palindrome("Racecar") is False
    assert is_palindrome("A man, a plan, a canal: Panama") is False
    assert is_palindrome("") is True
    assert is_palindrome("ab") is False
