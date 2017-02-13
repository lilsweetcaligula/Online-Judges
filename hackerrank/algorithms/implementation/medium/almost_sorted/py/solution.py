def solution(L):
    def isAscending(L):
        m = 1

        while m < len(L):
            if L[m] < L[m - 1]:
                return False
            m += 1

        return True

    buffer = list(L[:])
    i = 1

    while i < len(buffer):
        if buffer[i] < buffer[i - 1]:
            i -= 1
            break
        i += 1

    j = len(buffer) - 1

    while j > i:
        if buffer[j] < buffer[j - 1]:
            j += 1
            break
        j -= 1
    else:
        return 'yes', 0, 0
        
    buffer[i], buffer[j - 1] = buffer[j - 1], buffer[i]

    if isAscending(buffer):
        return 'swap', i + 1, j
    else:
        buffer[i], buffer[j - 1] = buffer[j - 1], buffer[i]

    k = i + 1

    while k < j:
        if buffer[k] > buffer[k - 1]:
            break
        k += 1
    else:
        buffer[i:j] = reversed(buffer[i:j])
        
        if isAscending(buffer):
            return 'reverse', i + 1, j
        else:
            return 'no', 0, 0

    return 'no', 0, 0

n         = int(input())
L         = list(map(int, input().split()))
ans, i, j = solution(L)

if ans == 'no' or ans == 'yes':
    print(ans)
else:
    print('yes')
    print(ans, i, j)
