#!/bin/python3

import sys

def solution(s):
    import itertools
    import math
    
    t        = s.replace(' ', '')

    sqrt     = math.sqrt(len(t))
    colCount = math.ceil(sqrt)
    rowCount = math.floor(sqrt)

    table    = []
    i        = 0

    while i < len(t):
        table.append(t[i:i + colCount].ljust(colCount))
        i += colCount

    return ' '.join(map(lambda x: ''.join(x).strip(), zip(*table)))

s = input().strip()
t = solution(s)

print(t)
