#!/bin/python

import ctypes

testCount = int(raw_input())
for testId in range(testCount):
    value = int(raw_input())
    flipped = ~value & 0xFFFFFFFF
    print flipped
