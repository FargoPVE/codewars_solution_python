def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


def odd_or_even_2(arr):
    if len(arr):
        if sum(arr) % 2 == 0:
            return "even"
        else:
            return 'odd'
    else:
        return 'even'
