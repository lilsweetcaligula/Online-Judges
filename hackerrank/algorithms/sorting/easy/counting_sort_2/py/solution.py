#!/bin/python

def calculateFrequencies(L, lowerBound = 0, upperBound = 100):
    aux = {}
    for value in L:
        if value in aux:
            aux[value] += 1
        else:
            aux[value] = 1
    freqs = {}
    for value in range(lowerBound, upperBound):
        if value in aux:
            freqs[value] = aux[value]
        else:
            freqs[value] = 0
    return freqs

def countingSort(L):
    lowerBound, upperBound = min(L), max(L) + 1
    freqs = calculateFrequencies(L, lowerBound, upperBound)
    aux = set(L)
    count = 0
    for value in range(lowerBound, upperBound):
        if value in aux:
            for j in range(freqs[value]):
                L[count] = value
                count += 1
                
size = int(raw_input())
L = [int(value) for value in raw_input().split()[:size]]
countingSort(L)
print " ".join(str(value) for value in L)
