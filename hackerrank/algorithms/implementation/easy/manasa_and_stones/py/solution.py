def solution(n, a, b):
    values = set()

    for amul in range(n):
        bmul = n - 1 - amul
        values.add(amul * a + bmul * b)

    return values

testCount = int(input())

for testId in range(testCount):
    n, a, b = map(int, (input() for i in range(3)))
    result  = sorted(solution(n, a, b))

    print(' '.join(map(str, result)))
