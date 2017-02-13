#!/bin/python3

import sys
import collections

n = int(input().strip())
c = map(int, input().strip().split(' '))

pairCount = sum(count // 2 for count in collections.Counter(c).values())

print(pairCount)
