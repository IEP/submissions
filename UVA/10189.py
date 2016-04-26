#!/bin/python

def check(y,x):
    global b, k, d
    if y == -1 or y == b or x == -1 or x == k:
        return False
    if d[y][x] == '*':
        return True

def flood(y,x):
    global d
    if d[y][x] != '*':
        counter = 0
        if check(y-1,x-1): counter += 1
        if check(y-1,x): counter += 1
        if check(y-1,x+1): counter += 1
        if check(y,x-1): counter += 1
        if check(y,x+1): counter += 1
        if check(y+1,x-1): counter += 1
        if check(y+1,x): counter += 1
        if check(y+1,x+1): counter += 1
        counter = str(counter)
        d[y][x] = counter

c = 1

while True:
    try:
        s = str(input())
        if s == '0 0':
            raise EOFError
        if c > 1:
            print()
        b, k = list(map(int,s.split()))
        d = [list(str(input())) for i in range(b)]
        for i in range(b):
            for j in range(k):
                flood(i,j)
        print('Field #{}:'.format(c))
        for i in d:
            print(''.join(i))
        c += 1
    except EOFError:
        break
