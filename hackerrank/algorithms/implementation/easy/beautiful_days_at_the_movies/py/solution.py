def beau(i, j, k):
    vals = []

    for x in range(i, j + 1):
        y = int(str(x)[::-1])
        
        if abs(x - y) % k == 0:
            vals.append(x)
            
    return len(vals)

i, j, k = map(int, input().split())
count   = beau(i, j, k)

print(count)
