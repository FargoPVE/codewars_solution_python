def delete_nth(order, max_e):
    out_list = []
    for number in order:
        if out_list.count(number) >= max_e:
            continue
        else:
            out_list.append(number)
    return out_list