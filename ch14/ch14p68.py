#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return input()
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
a, b, k, x = read()
def f(a,b,x,k):
    ans = abs(a*x + b)
    if k == 1:
        return ans
    return f(a,b,ans,k-1)
o = f(a,b,x,k)
print(o)
