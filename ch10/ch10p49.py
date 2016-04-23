#!/bin/python
f = lambda a, b, x : abs(a*x + b)
def fun(a,b,k,x):
    if k == 1:
        return f(a,b,x)
    return fun(a,b,k-1,f(a,b,x))
def mapper(x):
    return list(map(int, x))
n = mapper(input().split())
print(fun(n[0],n[1],n[2],n[3]))
