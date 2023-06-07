#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char)-32) if ord(char) > 96 and ord(char) < 123
              else "{:c}".format(ord(char)), end='')
    print()
