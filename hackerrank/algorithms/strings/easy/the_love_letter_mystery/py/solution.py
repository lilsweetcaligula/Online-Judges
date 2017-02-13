def solution(s):
    chars = list(s)
    count = 0
    i     = 0
    j     = len(chars) - 1

    while i < j:
        while chars[i] != chars[j]:
            if chars[i] < chars[j]:
                chars[i] = chr(ord(chars[i]) + 1)
            else:
                chars[j] = chr(ord(chars[j]) + 1)
            count += 1
        i += 1
        j -= 1

    return count

testCount = int(input())

for testId in range(testCount):
    string = input().strip()
    count  = solution(string)
    
    print(count)
