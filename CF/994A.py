#!/usr/bin/env python
n, m = map(int, input().split())
seq = map(int, input().split())
finger = list(map(int, input().split()))

ans = []
for i in seq:
    if i in finger:
        ans.append(i)

print(' '.join(map(str, ans)))