#!/usr/bin/python3
from sys import argv

for i in range(1, len(argv)):
    print("{:d}: {:s}".format(i, argv[i]))
