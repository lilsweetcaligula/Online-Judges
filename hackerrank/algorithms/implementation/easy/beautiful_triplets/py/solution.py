def beau(vals, diff):
    lookup = set(vals)
    result = []

    for x in vals:
        if x - diff in lookup and x + diff in lookup:
            result.append((x - diff, x, x + diff))

    return result

n, d     = map(int, input().split())
values   = tuple(map(int, input().split()))
triplets = beau(values, d)

print(len(triplets))
