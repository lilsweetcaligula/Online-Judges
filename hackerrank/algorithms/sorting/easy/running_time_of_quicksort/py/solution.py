#!/bin/python

class QuickSort(object):
    def __init__(self, debugMode = False):
        self._debugMode = debugMode
        self._swapCount = 0
    
    def partition(self, L, lo, hi):
        if hi - lo < 2:
            return lo
        i = j = lo
        v = hi - 1
        while i < v:
            if L[i] < L[v]:
                L[i], L[j] = L[j], L[i]
                if self._debugMode: self._swapCount += 1
                j += 1
            i += 1
        L[j], L[v] = L[v], L[j]
        if self._debugMode: self._swapCount += 1
        return j
   
    def sort(self, L):
        def helper(L, lo, hi):
            if hi - lo < 2:
                return lo
            v = self.partition(L, lo, hi)
            helper(L, lo, v)
            helper(L, v + 1, hi)
        helper(L, 0, len(L))
        
class InsertionSort(object):
    def __init__(self, debugMode = False):
        self._debugMode = debugMode
        self._swapCount = 0
    
    def sort(self, L):
        for i in range(len(L)):
            key = L[i]
            for j in reversed(range(i)):
                if L[j] < key:
                    break
                L[j], L[j + 1] = L[j + 1], L[j]
                if self._debugMode: self._swapCount += 1
        
size = int(raw_input())
L = [int(value) for value in raw_input().split()]
        
sortingAlgos = InsertionSort(True), QuickSort(True)
swapCounts = []
for algo in sortingAlgos:
    LCopy = L[:]
    algo.sort(LCopy)
    swapCounts.append(algo._swapCount)
for i in range(len(swapCounts) - 1):
    print swapCounts[i] - swapCounts[i + 1]
