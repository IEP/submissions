#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
score = (3,1,0)
def check(x, n):
    win = lose = n*(n-1)//2
    tie = 0
    for i in x:
        match = n - 1
        if i > score[0] * match:
            return False
        if i >= score[0]:
            temp = i // score[0]
            win -= temp
            match -= temp
            i -= score[0] * temp
        if i >= score[1]:
            temp = i // score[1]
            tie += temp
            match -= temp
            i -= score[1] * temp
        if match > 0:
            lose -= match
        if win < 0 or lose < 0
            return False
    return True
for T in range(int(read(0))):
    temp = read()
    N = temp[0]
    d = temp[1:]
    print('YES' if check(d, N) else 'NO')
