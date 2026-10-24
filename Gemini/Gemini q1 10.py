def is_palindrome(s: str) -> bool:
    """Returns True if the string reads the same forwards and backwards."""
    return s == s[::-1]

