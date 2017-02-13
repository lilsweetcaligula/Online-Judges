def solution(s):
    import collections
    
    left, right = s[:len(s) // 2], s[len(s) // 2:]
        
    if len(left) != len(right):
        return -1

    lookup = collections.Counter(left)

    count = 0
    
    for rc in right:
        if rc in lookup and lookup[rc] > 0:
            lookup[rc] -= 1
        else:
            count += 1

    return count

testCount = int(input())

for testId in range(testCount):
    source = input().strip()
    count  = solution(source)
    
    print(count)
