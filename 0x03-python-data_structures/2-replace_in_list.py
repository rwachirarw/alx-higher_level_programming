#!/usr/bin/pyhton3


def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx < 0) or (idx > length - 1):
        return my_list
    for i in range(0, length):
        if i == idx:
            my_list[i] = element
            return my_list
