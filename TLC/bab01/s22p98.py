#!/usr/bin/env python3
n = int(input())
t = 1
for i in range(1,n+1):
    print(' ' * (n - t) + '*' * t)
    t += 1
