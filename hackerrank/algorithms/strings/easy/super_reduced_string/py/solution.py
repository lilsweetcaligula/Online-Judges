def solution(s):
    while True:
        t = ''
        i = 0
        c = 0

        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                i += 2
                c += 1
            else:
                t += s[i]
                i += 1

        s = t

        if c == 0:
            break

    return s
        

source  = input().strip()
reduced = solution(source)

if reduced:
    print(reduced)
else:
    print('Empty String')
