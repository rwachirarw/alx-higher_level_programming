#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = []
    for i in range(0, len(str)):
        if (i != n):
            str_cpy.append(str[i])
    return (''.join(str_cpy))

