#!/bin/python3

import sys

def solution(signal):
    import itertools
    
    count = 0
    
    for expected, received in zip(itertools.cycle('SOS'), signal):
        if expected != received:
            count += 1
        
    return count

signal = input().strip()
count  = solution(signal)

print(count)
