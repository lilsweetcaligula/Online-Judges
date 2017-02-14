#!/bin/python3

import sys

def solution(n):
    if n == 0:
        return 1
    return 2 ** len([bit for bit in bin(n)[2:] if bit == '0'])

n = int(input().strip())
c = solution(n)

print(c)
