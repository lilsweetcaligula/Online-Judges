#!/bin/python3

import sys

def rotr(seq, cnt):
    if len(seq) == 0:
        return seq[:]

    k       = cnt % len(seq)
    seq[:]  = reversed(seq)
    seq[:k] = reversed(seq[:k])
    seq[k:] = reversed(seq[k:])

    return seq

n,k,q = input().strip().split(' ')
n,k,q = map(int, (n, k, q))
a     = list(map(int, input().strip().split(' ')[:n]))

for a0 in range(q):
    m = int(input().strip())
    print(a[m - k % len(a)])
