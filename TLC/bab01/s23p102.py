#!/usr/bin/env python3
n = int(input())
if 0 <= n <= 10:
    total = 1
    for i in range(1,n+1):
        total *= i
    print(total)
else:
    print('ditolak')
