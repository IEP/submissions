#!/bin/python
import sys
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = handle.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
T = int(read(0))

vowel = ['A', 'E', 'I', 'O', 'U']
def check2(s,v=vowel):
    if s[0] not in v and s[1] not in v:
        return True
def check3(s,v=vowel):
    if s[0] in v and s[1] in v and s[2] in v:
        return True
def solve(kata,case):
    panjang = len(kata)
    score = 0
    for i in range(2,panjang+1):
        temp = kata[i-2:i]
        if check2(temp):
            score += 1
    for i in range(3,panjang+1):
        temp = kata[i-3:i]
        if check3(temp):
            score += 1
    o = 'EASY' if score == 0 else score
    print('Case #{}: {}'.format(case, o))

for i in range(T):
    s = str(read(0))
    solve(s,i+1)
