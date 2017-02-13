#!/bin/python3

import sys


s, t    = map(int, input().strip().split(' '))
a, b    = map(int, input().strip().split(' '))
m, n    = map(int, input().strip().split(' '))

apples  = tuple(map(int, input().strip().split(' ')))
oranges = tuple(map(int, input().strip().split(' ')))

appleCount  = len(tuple(filter(lambda dist: s <= a + dist <= t, apples)))
orangeCount = len(tuple(filter(lambda dist: s <= b + dist <= t, oranges)))

print(appleCount)
print(orangeCount)
