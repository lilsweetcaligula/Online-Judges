#!/bin/python3

import sys


n, t  = map(int, input().split())
width = list(map(int, input().split()))

for a0 in range(t):
    i, j = map(int, input().strip().split(' '))
    veh  = min(width[i:j + 1])
    
    print(veh)
