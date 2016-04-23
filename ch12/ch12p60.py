#!/bin/python
def m(x):
    return list(map(int,x))
a = input()
d = m(input().split())
for i in range(int(input())):
    f = m(input().split())
    t = 0
    for j in range(awal(),len(d)):
        if d[j] > f[0] and d[j] <= f[1]:
            t += 1
        elif d[j] > f[1]:
            break
    print(t)
