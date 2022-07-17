def unique_in_order(iterable):
    result_out_list = []
    previously_value = None
    for char in iterable[0:]:
        if char != previously_value:
            result_out_list.append(char)
            previously_value = char
    return result_out_list