#!/bin/python3

import sys

def solution(time):
    import math as m
    
    computeCycleByTime    = lambda time:  m.floor(m.log2(((time - 1) / 3) + 1))
    computeCycleStartTime = lambda cycle: 3 * (2 ** (cycle) - 1) + 1
    computeCyclePeriod    = lambda cycle: 3 * 2 ** cycle
    
    cycle                 = computeCycleByTime(time)
    cycleStartTime        = computeCycleStartTime(cycle)
    cyclePeriod           = computeCyclePeriod(cycle)

    return cyclePeriod - (time - cycleStartTime)

t = int(input())
v = solution(t)

print(v)
