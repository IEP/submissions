#!/bin/python
def prime(x):
    atas = int(x**0.5)
    if x < 2:
        return False
    for i in range(2,atas+1):
        if x % i == 0:
            return False
    return True

def hitung(x):
    global q
    t = 0
    for i in q:
        if i == x:
            t += 1
    return t

n = int(input())

a = 2
q = []
while n >= a:
    if prime(a) and n % a == 0:
        n /= a
        q.append(a)
    else:
        a += 1

o = ''
last = 0
for i in q:
    if i == last:
        continue
    else:
        if hitung(i) > 1:
            o += '{}^{}'.format(i,hitung(i))
        elif hitung(i) == 1:
            o += '{}'.format(i)
        last = i
        if i < q[len(q)-1]:
            o += ' x '
print(o)
