#!/usr/bin/python3


def multiple_returns(sentence):
    while sentence:
        return(len(sentence), sentence[0])
    return(0, 'None')
