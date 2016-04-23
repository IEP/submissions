#!/bin/python
n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
d.sort()
if n % 2 == 0:
    ans = (d[n//2-1] + d[n//2])/2
else:
    ans = d[n//2]
ans = float(ans)
print(ans)
