#!/bin/python
def prime(x):
    atas = int(x**0.5)
    if x < 2:
        return False
    elif x == 2:
        return True
    for i in range(2,atas+1):
        if x % i == 0:
            return False
    return True

n = int(input())

a = 2
q = []
while n >= a:
    if prime(a) and n % a == 0:
            n /= a
            q.append(a)
    else:
        a += 1

w = []
for i in range(q[len(q)-1]+1):
    if q.count(i):
        w.append([i,q.count(i)])

o = ''
for i in range(len(w)):
    if w[i][1] > 1:
        o += '{}^{}'.format(w[i][0],w[i][1])
    else:
        o += '{}'.format(w[i][0])
    if i < len(w)-1:
        o += ' x '
print(o)
