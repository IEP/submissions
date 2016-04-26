#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
while True:
    try:
        d = read()
        cycle = 1
        for i in range(d[0],d[1]+1):
            c = 1
            n = i
            while n != 1:
                if n % 2 == 0:
                    n = n//2
                else:
                    n = 3*n + 1
                c += 1
            if c > cycle:
                cycle = c
        print('{} {} {}'.format(d[0],d[1],cycle))
    except EOFError:
        break
