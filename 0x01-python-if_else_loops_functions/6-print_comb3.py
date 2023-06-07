#!/usr/bin/python3
for i in range(1, 88):
    if (i < int(str(i)[::-1])) or (i < 10):
        print("{:02d}".format(i), end=', ')
    else:
        print('', end='')
print('89')
