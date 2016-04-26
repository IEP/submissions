#!/bin/python
while True:
    try:
        n, k = list(map(int,input().strip().split()))
        t = n
        while n >= k:
            t += n//k
            n = n//k
        print(t)
    except EOFError:
        break
