#!/bin/python3

import sys

def solution(s):
    pattern   = '010'
    positions = []
    index     = s.find(pattern)
    
    while index >= 0:
        positions.append(index)
        index = s.find(pattern, index + 1)
    
    count = 0
    index = 0
    
    while index < len(positions):
        count += 1
              
        if index + 1 < len(positions) and abs(positions[index] - positions[index + 1]) < len(pattern):
            index += 1

        index += 1
        
    return count
    
n = int(input())
B = input().strip()
c = solution(B)

print(c)
