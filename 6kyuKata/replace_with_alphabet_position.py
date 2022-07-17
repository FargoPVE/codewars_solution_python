def alphabet_position(text):
    ord_out_list = []
    for char in list(text.lower()):
        if char.isalpha():
            ord_out_list.append(ord(char) - 96)
        else:
            continue
    return ' '.join(map(str, ord_out_list))