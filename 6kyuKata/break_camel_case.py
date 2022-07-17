def solution(s):
    test_list_for_iteration = []
    for enum in s:
        if enum.isupper():
            test_list_for_iteration.append(' ')
            test_list_for_iteration.append(enum)
        else:
            test_list_for_iteration.append(enum)
    return ''.join(test_list_for_iteration)