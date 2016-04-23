#!/bin/python
def df(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        a = n//2
    else:
        a = n
    return a * df(n-1)
n = int(input())
ans = df(n)
print(ans)
