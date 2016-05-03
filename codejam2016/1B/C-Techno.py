#!/usr/bin/env python3
for T in range(int(input())):
    first = {}
    second = {}
    for N in range(int(input())):
        a, b = input().split()
        first[a] = first.get(a,0) + 1
        second[b] = second.get(b,0) + 1
    x = y = 0
    for i, j in zip(first.values(), second.values()):
        if i > 1:
            x += (i-1)
        if j > 1:
            y += (j-1)
    res = min(x,y)
    print('Case #{}: {}'.format(T+1,res))
