#!/bin/python3

import sys

def bsearch_left(L, x, key=None, lo=None, hi=None):
    if key == None:
        key = lambda x: x

    if lo == None:
        lo = 0
        
    if hi == None:
        hi = len(L)

    begin = lo
    end   = hi
        
    while lo < hi:
        mid = lo + (hi - lo) // 2
            
        if key(L[mid]) >= x:
            hi = mid
        elif key(L[mid]) < x:
            lo = mid + 1
             
    if begin <= lo < end and key(L[lo]) == x:
        return lo

    return -1

def computeNumOfPairs(values, k):
    import bisect

    if len(values) == 0:
        return []

    # We need to keep indices of the values in the array in tact, at the
    # same time we want to speed things up with the bisection algorithm.
    # We employ the pointer array trick in which we generate indices and
    # sort the array of indices based on the values in the original 
    # array.
    indices = sorted(range(len(values)), key=lambda x: values[x])
    
    # Generate all possible values evenly divisible by k in range:
    # [minval, ..., maxval]
    #
    # We start the range with the value closest to min(value) which is
    # a multiple of k.
    #
    # We end the range with a value twice as big as max(values) which
    # is a multiple of k.
    minval    = min(values)
    maxval    = max(values)
    divisible = tuple(range(k - minval % k + minval, 2 * maxval + 1, k))

    if len(divisible) == 0:
        # No divisible values possible with the values given in the array.
        # Peace out.
        return []

    result = []
    
    for i, x in enumerate(values):
        # Find the smallest possible divisor larger or equal to x.
        # We use the bisection algorithm to speed things up.
        j = bisect.bisect_left(divisible, x)
                
        if not 0 <= j < len(divisible):
            # Impossible since max(values) is twice as small as the largest
            # divisor in the divisible tuple. We leave this check here in
            # case of future edits nonetheless.
            break

        while j < len(divisible):
            # Search all values that can be produced by the sum of the current
            # value with another value. Whether this "another" value exists or
            # not, we check at a later point using the bisection algorithm.
            div = divisible[j]

            if div >= x:
                # div - x is the "another" value we need to add to the current
                # value in order to produce a value divisible by k. Check if it's
                # in the array.
                y = div - x
                k = bsearch_left(indices, y, key=lambda x: values[x])

                if k != -1:
                    while k < len(indices) and values[indices[k]] == y:
                        if indices[k] > i:
                            result.append((i, indices[k]))
                        k += 1

                j += 1

    return result
    

n, k  = map(int, input().strip().split(' '))
a     = tuple(map(int, input().strip().split(' ')))

count = len(computeNumOfPairs(a, k))

print(count)
