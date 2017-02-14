#!/bin/python

def zeroBalanceSum(L):
    lsums = []
    total = 0
    for item in L:
        lsums.append(total)
        total += item
        
    rsums = []        
    total = 0
    for item in reversed(L):
        rsums.append(total)
        total += item
    rsums.reverse()

    for i in range(len(L)):
        if lsums[i] == rsums[i]:
            return True
    return False

testCount = int(raw_input())
for testId in range(testCount):
    size = int(raw_input())
    L = [int(value) for value in raw_input().split()]
    if zeroBalanceSum(L):
        print 'YES'
    else:
        print 'NO'
