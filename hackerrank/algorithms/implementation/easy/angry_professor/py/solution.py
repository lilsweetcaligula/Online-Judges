#!/bin/python3

import sys

def isClassCancelled(arrivalTimes, cancellationThreshold):
    count = 0
    
    for arrivalTime in arrivalTimes:        
        if arrivalTime <= 0:
            count += 1
            
    return count < cancellationThreshold

t = int(input())

for a0 in range(t):
    n, k = map(int, input().split())
    a    = tuple(map(int, input().split()))
    
    if isClassCancelled(a, k):
        print('YES')
    else:
        print('NO')
