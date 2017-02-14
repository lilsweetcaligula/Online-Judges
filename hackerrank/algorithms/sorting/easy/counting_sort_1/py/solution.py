#!/bin/python

def calculateFrequencies(L, lowerBound=0, upperBound=100):
    freqs = {}
    for value in range(lowerBound, upperBound):
        freqs[value] = 0
        for i in range(len(L)):
            if L[i] == value:
                if value in freqs:
                    freqs[value] += 1
    return freqs

size = int(raw_input())
L = [int(value) for value in raw_input().split()[:size]]
freqs = calculateFrequencies(L)
for key in range(101):
    print freqs[key],
print '\n'
