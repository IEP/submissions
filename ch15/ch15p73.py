#!/bin/python
from copy import copy
def per(a, b):
    if len(b) == 0:
        print(''.join(map(str,a)))
    for i in b:
        p, q = copy(a), copy(b)
        p.append(i)
        q.remove(i)
        if len(a) > 1:
            mid = a[len(a)-1]
            left = a[len(a)-2]
            right = i
            if left > mid < right:
                per(p,q)
            elif left < mid > right:
                per(p,q)
        else:
            per(p,q)
n = int(input())
d = [i for i in range(1, n+1)]
per([], d)
