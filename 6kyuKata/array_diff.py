def array_diff(a, b):
    for i in b:
        if i in a:
            for item in range(a.count(i)):
                a.remove(i)
    return a