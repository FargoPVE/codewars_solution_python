def find_next_square(sq):
    sqr = sq ** 0.5
    if sqr % 1 == 0:
        return (sqr + 1) * (sqr + 1)
    else:
        return -1