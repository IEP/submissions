#!/bin/python
def pal(x):
    return int(str(x)[::-1])
T = int(input())
for i in range(T):
    n = int(input())
    m = pal(n)
    c = 0
    while n != m:
        n = m + n
        m = pal(n)
        c += 1
    print('{} {}'.format(c, n))

