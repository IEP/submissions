#!/bin/python
from itertools import combinations
n, k = map(int, input().strip().split())
d = [i for i in range(1,n+1)]
d = ''.join(map(str,d))
for i in combinations(d,k):
    print(' '.join(map(str,i)))
