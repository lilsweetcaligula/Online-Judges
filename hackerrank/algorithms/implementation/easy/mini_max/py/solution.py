#!/bin/python

import sys

DEBUG   = False

nums    = list(map(int, input().strip().split(' ')))

if DEBUG:
  assert(len(nums) == 5)

ordered = sorted(nums)
minSum  = sum(ordered[:-1])
maxSum  = sum(ordered[1:])

print(minSum, maxSum)
