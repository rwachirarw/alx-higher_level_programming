#!/usr/bin/python3
def uppercase(str):
    string = []
    for char in str:
        if (ord(char) > 96 and ord(char) < 123):
            string.append(chr(ord(char) - 32))
        else:
            string.append(char)
    print(''.join(string))
