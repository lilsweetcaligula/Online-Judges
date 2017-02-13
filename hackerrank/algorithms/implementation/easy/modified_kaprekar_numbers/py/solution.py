def iskaprekar(x):
    digits = str(x ** 2)
    left   = digits[:len(digits) // 2]
    right  = digits[len(digits) // 2:]
    return x == (int(left) if left else 0) + (int(right) if right else 0)

def solution(p, q):
    return tuple(filter(iskaprekar, range(p, q + 1)))

p    = int(input())
q    = int(input())
kapr = solution(p, q)

print(' '.join(map(str, kapr)) if kapr else 'INVALID RANGE')
