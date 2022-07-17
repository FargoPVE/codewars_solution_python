def duplicate_encode(word):
    split_word_list = [i for i in word.lower()]
    out_list = []
    for i in split_word_list:
        if split_word_list.count(i) == 1:
            out_list.append('(')
        else:
            out_list.append(')')
    return ''.join(out_list)