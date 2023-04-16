import sys
input = sys.stdin.readline
n = int(input())
t = []
p = []
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
profit = [0] * (n+1)
max_value = 0 
for i in range(n):
    max_value = max(max_value, profit[i]) 
    if i+t[i] <= n:
        profit[i+t[i]] = max(profit[i+t[i]],max_value+p[i])
print(max(profit))