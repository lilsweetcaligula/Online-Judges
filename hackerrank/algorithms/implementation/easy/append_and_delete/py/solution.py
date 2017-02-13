#!/bin/python3

import sys

def canConvert(s, t, k):    
    cmnPrefixCnt = 0

    for c1, c2 in tuple(zip(s, t)):
        if c1 == c2:
            cmnPrefixCnt += 1
        else:
            break

    minDelCnt = len(s) - cmnPrefixCnt
    minAddCnt = len(t) - cmnPrefixCnt
    
    if k >= len(s) + len(t):
        return True
    else:    
        addCnt = minAddCnt

        for delCnt in range(minDelCnt, len(s) + 1):
            chgCnt = addCnt + delCnt

            if chgCnt == k:
                return True
            elif chgCnt > k:
                return False

            addCnt += 1

    return False
    
s = input().strip()
t = input().strip()
k = int(input())

if canConvert(s, t, k):
    print('Yes')
else:
    print('No')
