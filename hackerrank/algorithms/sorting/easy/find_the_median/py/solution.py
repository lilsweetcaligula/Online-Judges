#!/bin/python

def partition(L, lo, hi):
    # Lomuto partitioning.
    #
    i = j = lo
    v = hi - 1
    while i < hi:
        if L[i] < L[v]:
            L[i], L[j] = L[j], L[i]
            j += 1
        i += 1
    L[v], L[j] = L[j], L[v]
    return j

def median(L):
    # Hoare's quick select.
    #
    if len(L) == 0:
        raise ValueError("Empty sequence.")
    lo = 0
    hi = len(L)
    while lo < hi:
        v = partition(L, lo, hi)
        if v < len(L) // 2:
            lo = v + 1
        elif v > len(L) // 2:
            hi = v
        else: 
            break
    return L[v]

size = int(raw_input())
L = [int(value) for value in raw_input().split()]
m = median(L)
print m
