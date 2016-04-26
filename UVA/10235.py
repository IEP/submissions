#!/bin/python
prime = [True] * 1000000
prime[0] = False
prime[1] = False
for i in range(2,1000):
    for j in range(i*i,1000000,i):
        if prime[j]:
            prime[j] = False
while True:
    try:
        n = int(input())
        m = int(str(n)[::-1])
        if prime[n] and prime[m] and m != n:
            print('{} is emirp.'.format(n))
        elif prime[n]:
            print('{} is prime.'.format(n))
        else:
            print('{} is not prime.'.format(n))
    except EOFError:
        break
