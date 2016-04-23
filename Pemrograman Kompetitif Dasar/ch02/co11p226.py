#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)
def lcm(a,b):
    return a // gcd(a,b) * b
x = read()
y = read()
den = lcm(x[1],y[1])
num = den // x[1] * x[0] + den // y[1] * y[0]
sf = gcd(den,num)
den //= sf
num //= sf
print('{} {}'.format(num,den))
