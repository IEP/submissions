#!/usr/bin/env python3
def semiPrime(n):
    if n < 1: return False
    flag = False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            if not flag:
                flag = True
            else:
                return False
    return True
for T in range(int(input())):
    n = int(input())
    print('YA' if semiPrime(n) else 'TIDAK')
