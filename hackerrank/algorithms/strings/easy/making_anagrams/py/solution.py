def solution(s, t):
    import collections
    import itertools

    cs = collections.Counter(s)
    ct = collections.Counter(t)

    count = 0
    
    for c in set(itertools.chain(s, t)):
        count += abs(cs[c] - ct[c])

    return count

s = input().strip()
t = input().strip()
c = solution(s, t)

print(c)
