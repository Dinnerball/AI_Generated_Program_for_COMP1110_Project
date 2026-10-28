def word_frequency(text):
    from collections import Counter
    return dict(Counter(text.lower().split()))