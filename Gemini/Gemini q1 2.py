def is_palindrome(s: str) -> bool:
    # 严格区分大小写和标点，直接首尾对比
    return s == s[::-1]

