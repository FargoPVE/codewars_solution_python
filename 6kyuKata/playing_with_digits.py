def dig_pow(n, p):
    assert n > 0 and p > 0
    digits = (int(i) for i in str(n))
    result = 0
    for x in digits:
        result += x ** p
        p += 1

    if result % n:
        return -1
    else:
        return result // n