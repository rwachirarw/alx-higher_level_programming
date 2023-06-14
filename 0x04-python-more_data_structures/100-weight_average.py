#!/usr/bin/python3
def weight_average(my_list=[]):
    list_sum = []
    for i in my_list:
        list_sum += (i[0] * i[1])
    return list_sum
