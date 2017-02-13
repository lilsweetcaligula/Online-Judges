def solution(s, t):
    for c in s:
        if c in t:
            return True
            
    for c in t:
        if c in s:
            return True

    return False

testCount = int(input())

for testId in range(testCount):
    s = input().strip()
    t = input().strip()

    if solution(s, t):
        print('YES')
    else:
        print('NO')
