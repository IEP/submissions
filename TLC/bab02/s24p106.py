#!/bin/python
d = {}
m = -1
N = int(input())
for i in range(N):
    temp = int(input())
    d[temp] = d.get(temp,0) + 1
a = max(d.values())
for i, j in d.items():
    if j == a:
        m = max(i,m)
print(m)
