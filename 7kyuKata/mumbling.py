def accum(s):
    result_list = []
    for j, i in enumerate(s):
        if i.islower() == True:
            result_list.append(i.upper() + i * j)
        else:
            result_list.append(i + (i.lower() * j))
    return '-'.join(result_list)
