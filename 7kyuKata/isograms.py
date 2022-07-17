def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)