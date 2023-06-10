#!/usr/bin/python3


def max_integer(my_list=[]):
    while my_list:
        my_list.sort()
        return (my_list[-1])
    return('None')
