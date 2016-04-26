#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def f(n):
    res = 1
    if res == 0:
        return 1
    for i in range(1,n+1):
        res *= i
    return res

def combi(n,k):
    mid = max(k,n-k)
    low = min(k,n-k)
    res = 1
    for i in range(mid+1,n+1):
        res *= i
    res //= f(low)
    return res

while True:
    n, k = read()
    if n == 0 and k == 0:
        break
    print(combi(n,k))
