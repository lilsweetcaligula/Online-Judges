#!/bin/python

def insertionSort(ar):
    DBG = True
    for i in xrange(len(ar)):
        key = ar[i]
        for j in reversed(xrange(i)):
            if ar[j] < key:
                break
            temp = ar[j + 1]
            ar[j + 1] = ar[j]
            if DBG: print " ".join(str(value) for value in ar)
            ar[j] = temp
    if DBG: print " ".join(str(value) for value in ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
