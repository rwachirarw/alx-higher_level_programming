#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = sum(score * weight for score, weight in my_list)
        denominator = sum(weight for _, weight in my_list)
        return numerator / denominator
    return 0
