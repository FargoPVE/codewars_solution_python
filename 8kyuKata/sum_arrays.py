def sum_array(a):
    if len(a) <= 0:
        return 0
    else:
        return sum(a[i] for i in range(0, len(a)))