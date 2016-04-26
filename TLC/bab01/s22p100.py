#!/usr/bin/env python3
n, k = map(int,input().split())
d = [str(i) if i % k != 0 else '*' for i in range(1,n+1)]
print(' '.join(d))
