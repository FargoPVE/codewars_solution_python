def get_middle(s):
    return s[int((len(s) - 1) / 2): int(len(s) / 2 + 1)]


def get_middle_2(s):
    if len(s) % 2 == 0:
        return s[int(len(s) // 2) - 1: int(len(s) // 2) + 1]
    else:
        return s[int(len(s) / 2)]
