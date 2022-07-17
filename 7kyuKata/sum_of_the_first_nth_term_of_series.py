def series_sum(n):
    if n == 0:
        return ("%.2f" % 0)
    else:
        n = n - 1
        sum_list = [1]
        while n > 0:
            x = 1 / float(n * 3 + 1)
            sum_list.append(x)
            n = n - 1
        return ("%.2f" % sum(sum_list))
