def printer_error(s):
    in_len = len(s)
    er_len = len([i for i in s if ord(i) < ord('a') or ord(i) > ord('m')])
    return str(er_len) + '/' + str(in_len)