def find_short(s):
    return min(map(len, [i for i in s.split()]))
