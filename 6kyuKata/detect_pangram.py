def is_pangram(text):
    return sum(1 for c in set(text.lower()) if 96 < ord(c) < 123) == 26