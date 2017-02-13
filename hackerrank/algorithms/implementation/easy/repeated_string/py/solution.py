#!/bin/python3

import sys

def repeated(s, n, c='a'):
    lookup = [0] * len(s)
    curcnt = 0
    
    for index, char in enumerate(s):
        if char == c:
            curcnt += 1

        lookup[index] = curcnt

    if n % len(s) == 0:
        return n // len(s) * curcnt
    
    return n // len(s) * curcnt + lookup[n - len(s) * (n // len(s)) - 1]

s = input().strip()
n = int(input())
c = repeated(s, n)

print(c)
