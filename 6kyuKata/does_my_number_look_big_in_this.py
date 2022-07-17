def narcissistic(value):
    positional_number_list = []
    split_number_list = [int(i) for i in str(value)]
    for i in split_number_list:
        positional_number_list.append(i ** len(split_number_list))
    return True if sum(positional_number_list) == value else False
