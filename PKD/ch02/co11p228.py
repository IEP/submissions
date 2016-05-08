#!/bin/python
def gcd(a,b):
    return a if b == 0 else gcd(b, a % b)
def lcm(a,b):
    return a // gcd(a,b) * b
T = int(input())
res = 1
for i in range(T):
    n = int(input())
    res = lcm(res,n)
print(res)
