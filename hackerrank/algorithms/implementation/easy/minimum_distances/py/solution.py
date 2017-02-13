#!/bin/python3

import sys

def minDistance(L):
    if len(L) == 0:
        raise ValueError('L is an empty sequence.')
    
    indices = sorted(range(len(L)), key=lambda x: L[x])
    minDist = -1
    
    for i in range(1, len(indices)):
        curr, prev = L[indices[i]], L[indices[i - 1]]
        
        if curr == prev:
            curDist = abs(indices[i] - indices[i - 1])
            minDist = min(minDist, curDist) if minDist != -1 else curDist
            
    return minDist

n = int(input())
L = tuple(map(int, input().split()))
d = minDistance(L)

print(d)
