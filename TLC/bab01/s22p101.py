#!/usr/bin/env python3
n = int(input())
d = []
for i in range(1,n+1):
    if n % i == 0:
        d.append(i)
d.sort(reverse=True)
print('\n'.join(map(str,d)))
