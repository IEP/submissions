#!/usr/bin/env python3
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a//gcd(a,b)*b

res = 1
for i in range(1,21):
    res = lcm(res,i)
print(res)
