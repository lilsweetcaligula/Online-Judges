#!/bin/python

def lessThanEqualCount(L, lowerBound = 0, upperBound = 100):
    counts = []
    for peak in range(lowerBound, upperBound):
        count = 0
        for value in L:
            if value <= peak:
                count += 1
        counts.append(count)
    return counts

count = int(raw_input())
values = []
for i in range(count):
    value = int(raw_input().split()[0])
    values.append(value)
lessThanEqualCounts = lessThanEqualCount(values)
print " ".join(str(value) for value in lessThanEqualCounts)
