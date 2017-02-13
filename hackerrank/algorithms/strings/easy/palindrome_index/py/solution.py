def solution(s):
    i = 0
    j = len(s) - 1
    
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            t = s[i + 1:j + 1]

            if t == t[::-1]:
                return i
            else:
                return j
    
    return -1

testCount = int(input())

for testId in range(testCount):
    s = input().strip()
    i = solution(s)
    
    print(i)
