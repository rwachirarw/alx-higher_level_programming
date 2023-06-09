#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    reversed_str = list(reversed(my_list))
    for i in range(0, len(reversed_str)):
        print("{:d}".format(reversed_str[i]))
