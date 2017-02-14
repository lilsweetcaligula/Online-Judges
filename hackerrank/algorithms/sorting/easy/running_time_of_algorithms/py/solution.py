#!/bin/python

def insertionSort(L):
    shiftCount = 0
    for i in range(len(L)):
        key = L[i]
        for j in reversed(range(i)):
            if L[j] <= key:
                break
            L[j], L[j + 1] = L[j + 1], L[j]
            shiftCount += 1
    return shiftCount

size = int(raw_input())
L = [int(value) for value in raw_input().split()]
shiftCount = insertionSort(L)
print shiftCount
