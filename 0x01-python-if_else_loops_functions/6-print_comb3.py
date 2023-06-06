#!/usr/bin/python3
for i in range(1, 98):
    if (i < int(str(i)[::-1])):
        print("{:02d}".format(i), end=', ')
    elif (i < 10):
        print("{:02d}".format(i), end=', ')
print("89")
