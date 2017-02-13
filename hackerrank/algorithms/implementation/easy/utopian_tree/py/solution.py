#!/bin/python3

import sys
import itertools

t = int(input())

for a0 in range(t):
    n = int(input())
    
    x = 1
    i = 0
    
    for f in itertools.cycle((lambda x: 2 * x, lambda x: x + 1)):
        if i >= n:
            break
        else:
            x  = f(x)            
            i += 1
            
    print(x)
