#!/bin/python

def bsearch(L, target):
    lo = 0
    hi = len(L)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if L[mid] > target:
            hi = mid
        elif L[mid] < target:
            lo = mid + 1
        else:
            return mid
    return -1        

target = int(raw_input())
size = int(raw_input())
L = [int(value) for value in raw_input().split()]
index = bsearch(L, target)
print index
