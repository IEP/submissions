#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
while True:
    case = int(read(0))
    if case == 0:
        break
    n, m = read()
    for i in range(case):
        x, y = read()
        x -= n
        y -= m
        if x == 0 or y == 0:
            print('divisa')
        elif x > 0 and y > 0:
            print('NE')
        elif x < 0 and y > 0:
            print('NO')
        elif x < 0 and y < 0:
            print('SO')
        elif x > 0 and y < 0:
            print('SE')
