#!/usr/bin/python3
for i in range(1, 10):
    num_str = "{:02d}".format(i)
    reversed_num = int(num_str[::-1])
    print(reversed_num)
