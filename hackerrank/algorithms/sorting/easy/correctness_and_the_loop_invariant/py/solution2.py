#!/bin/python

def insertion_sort(L):
    for i in xrange(1, len(L)):
        key = L[i]
        lo = 0
        hi = j = i
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if L[mid] > key:
                hi = mid
            else:
                lo = mid + 1
        L[lo + 1:j + 1] = L[lo:j]
        L[lo] = key

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
