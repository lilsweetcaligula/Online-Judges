#!/bin/python3

import sys


def solution(clouds, i=0, count=0):
    if i + 1 >= len(clouds):
        return count
    
    if clouds[i]:
        return False
    
    x = solution(clouds, i + 1, count + 1)
    y = solution(clouds, i + 2, count + 1)
          
    if not x:
        return y
    elif not y:
        return x
    
    return min(x, y)

n   = int(input().strip())
c   = [int(c_temp) for c_temp in input().strip().split(' ')]

res = solution(c)

print(res)
