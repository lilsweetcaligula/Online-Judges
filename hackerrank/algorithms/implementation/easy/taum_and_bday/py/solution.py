#!/bin/python3

import sys

def solution(b, x, w, y, z):
    amount = 0

    if x < y:
        amount += b * x

        if x + z < y:
            amount += w * (x + z)
        else:
            amount += w * y
    else:
        amount += w * y

        if y + z < x:
            amount += b * (y + z)
        else:
            amount += b * x

    return amount

t = int(input().strip())
for a0 in range(t):
    b, w    = map(int, input().split())
    x, y, z = map(int, input().split())
    result  = solution(b, x, w, y, z)
    
    print(result)
