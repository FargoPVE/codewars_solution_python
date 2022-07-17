def descending_order(num):
    out_list = [int(i) for i in str(num)]
    out_list.sort(reverse=True)
    return int(''.join((str(i) for i in out_list)))