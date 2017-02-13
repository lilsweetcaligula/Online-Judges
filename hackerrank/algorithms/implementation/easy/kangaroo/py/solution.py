#!/bin/python3

import sys

x1, v1, x2, v2 = map(int, input().strip().split(' '))

willLand = (
    v1 != v2
    and (x1 - x2) %  (v2 - v1) == 0 
    and (x1 - x2) // (v2 - v1) >= 0)

print(('NO', 'YES')[willLand])
