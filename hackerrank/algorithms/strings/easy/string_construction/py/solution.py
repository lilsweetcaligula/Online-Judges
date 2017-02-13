#!/bin/python3

import sys

def solution(source):
    return len(set(source))

n = int(input().strip())

for a0 in range(n):
    s = input().strip()
    c = solution(s)
    
    print(c)
