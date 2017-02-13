#!/bin/python3

import sys

# Hackerrank Python3 environment does not provide math.gcd
# as of the time of writing. We define it ourselves.
def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(x, y):
    return (x * y) // gcd(x, y)

def between(s1, s2):
    import functools

    cd = functools.reduce(gcd, s2)
    cm = functools.reduce(lcm, s1)

    return tuple(x for x in range(cm, cd + 1) if cd % x == 0 and x % cm == 0)

n, m = input().strip().split(' ')
n, m = [int(n),int(m)]
a    = [int(a_temp) for a_temp in input().strip().split(' ')]
b    = [int(b_temp) for b_temp in input().strip().split(' ')]

btw  = between(a, b)

print(len(btw))
