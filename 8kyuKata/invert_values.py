def invert(lst):
    return [-val for val in lst]


def invert_2(lst):
    output_list = []
    for char in lst:
        if char < 0:
            output_list.append(abs(char))
        else:
            output_list.append(-char)
    return output_list
