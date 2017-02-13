#!/bin/python3

import sys

def solution(n, c, m):
    cnt = n // c

    if m > 0:
        w = cnt

        while w >= m:
            x    = w // m
            w    = w - m * x + x
            cnt += x

    return cnt

t = int(input().strip())

for a0 in range(t):    
    n, c, m = map(int, input().split(' '))
    cnt     = solution(n, c, m)
    
    print(cnt)
