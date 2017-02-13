#!/bin/python3

import sys


def solution(hrs, min):
    lookup = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'quarter',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        21: 'twenty one',
        22: 'twenty two',
        23: 'twenty three',
        24: 'twenty four',
        25: 'twenty five',
        26: 'twenty six',
        27: 'twenty seven',
        28: 'twenty eight',
        29: 'twenty nine',
        30: 'half',
    }

    if min == 0:
        return "{} o' clock".format(lookup[hrs])
    elif min <= 30:
        if min == 15 or min == 30:
            return "{} past {}".format(lookup[min], lookup[hrs])
        else:
            return "{} minute{} past {}".format(lookup[min], '' if min == 1 else 's', lookup[hrs])        
    
    rem = 60 - min
    
    if rem == 15 or rem == 30:
        return "{} to {}".format(lookup[rem], lookup[hrs + 1])
    
    return "{} minute{} to {}".format(lookup[rem], '' if min == 1 else 's', lookup[hrs + 1])

h = int(input().strip())
m = int(input().strip())
s = solution(h, m)

print(s)
