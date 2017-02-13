def computeAnnaBill(k, costs):
    return sum(cost / 2.0 if index != k else 0.0 for index, cost in enumerate(costs))

eps     = 1e-12
n, k    = map(int, input().split())
costs   = [int(cost) for cost in input().split()]

charged = int(input())
actual  = computeAnnaBill(k, costs)

diff    = charged - actual

if abs(diff) < eps:
    print('Bon Appetit')
else:
    print('{:g}'.format(diff))
