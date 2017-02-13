def beau(vals, diff):
    lookup = set(vals)
    result = []

    for x in vals:
        if x - d in lookup and x + d in lookup:
            result.append((x - d, x, x + d))

    return result

n, d     = map(int, input().split())
values   = tuple(map(int, input().split()))
triplets = beau(values, d)

print(len(triplets))
