#!/bin/python

def missingNumbers(A, B):
    def getFreqs(L):
        freqs = {}
        for value in L:
            if value in freqs:
                freqs[value] += 1
            else:
                freqs[value] = 1
        return freqs
    aFreqs = getFreqs(A)
    bFreqs = getFreqs(B)
    missing = []
    for value in set(A + B):
        if ((value not in aFreqs or value not in bFreqs) 
            or (aFreqs[value] != bFreqs[value])):
            missing.append(value)
    return missing

firstInputLen = int(raw_input())
A = raw_input().split()[:firstInputLen]

secondInputLen = int(raw_input())
B = raw_input().split()[:secondInputLen]

missing = missingNumbers(A, B)
missing.sort()

for value in missing:
    print value,
print
