#!/bin/python
prime = [True] * 1500
prime[0] = prime[1] = False
for i in range(2,int(1500**0.5)+1):
    for j in range(i*i,1500,i):
        prime[j] = False
primeList = []
for i in range(len(prime)):
    if prime[i]:
        primeList.append(i)
def isPrime(n):
    if n < 1500:
        return prime[n]
    else:
        for i in primeList:
            if n % i == 0:
                return False
        return True
n = int(input())
factor = []
while not isPrime(n):
    for i in primeList:
        if n % i == 0:
            factor.append(i)
            n //= i
            break
factor.append(n)
temp = list(set(factor))
co = {}
for i in temp:
    co[i] = factor.count(i)
co = list(co.items())
co.sort(key=lambda x: x[0])
o = []
for i in co:
    if i[1] > 1:
        o.append('{}^{}'.format(i[0],i[1]))
    else:
        o.append('{}'.format(i[0]))
print(' x '.join(o))
