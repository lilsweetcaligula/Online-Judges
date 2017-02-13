#!/bin/python3

import sys

testCount = int(input())

for testId in range(testCount):
    n = int(input())
    c = len(tuple(filter(lambda x: x != 0 and n % x == 0, map(int, str(n)))))
    
    print(c)
