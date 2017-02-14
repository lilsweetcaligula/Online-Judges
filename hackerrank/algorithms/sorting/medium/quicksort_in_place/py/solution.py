#!/bin/python

class QuickSort(object):
    DBG = True
    
    @staticmethod
    def partition(L, lo, hi):
        if hi - lo < 2:
            return lo
        i = j = lo
        v = hi - 1
        while i < v:
            if L[i] < L[v]:
                L[i], L[j] = L[j], L[i]
                j += 1
            i += 1
        L[j], L[v] = L[v], L[j]
        return j
    
    @staticmethod
    def sort(L):
        def helper(L, lo, hi):
            if hi - lo < 2:
                return
            v = QuickSort.partition(L, lo, hi)
            if QuickSort.DBG: print " ".join(str(value) for value in L)
            helper(L, lo, v)
            helper(L, v + 1, hi)
        helper(L, 0, len(L))

size = int(raw_input())
L = [int(value) for value in raw_input().split()[:size]]
sorter = QuickSort()
sorter.sort(L)
