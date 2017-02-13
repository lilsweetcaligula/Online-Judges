#!/bin/python3

import sys
import bisect

n     = int(input())
arr   = sorted(map(int, input().split()))
begin = 0
count = len(arr)

while begin < len(arr):
    print(count)
        
    cut = arr[begin]
    i   = begin
    
    while i < len(arr):
        arr[i] -= cut
        
        if arr[i] == 0:
            count -= 1

        i += 1

    begin = bisect.bisect(arr, arr[begin])
