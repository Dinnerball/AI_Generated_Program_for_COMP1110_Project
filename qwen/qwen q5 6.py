def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq