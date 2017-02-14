#!/bin/python

def isPowOf2(value):
    return ((value & (value - 1)) == 0)

def getPrevPowOf2(value):
    count = 0
    m = 1
    while m < value:
        count += 1
        m <<= 1
    return 1 << (count - 1)

def counter(n):
    playerid = 0
    while n > 1:
        if isPowOf2(n):
            n -= n // 2
        else:            
            n -= getPrevPowOf2(n)
        playerid ^= 1
    return playerid ^ 1

testCaseCount = int(raw_input())
for testid in range(testCaseCount):
    n = int(raw_input())
    playerid = counter(n)
    if playerid == 0:
        print "Louise"
    else:
        print "Richard"
