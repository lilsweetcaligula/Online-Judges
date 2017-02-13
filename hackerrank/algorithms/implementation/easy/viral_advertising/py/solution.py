n = int(input())
p = 5
t = 0

for i in range(n):
    t += p // 2
    p  = 3 * (p // 2)
    
print(t)
