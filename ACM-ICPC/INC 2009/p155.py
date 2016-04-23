#!/bin/python
import sys
import itertools
f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
def read(mode=2,handle=f):
    inp = f.readline().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

def solve(board):
    le = len(board)
    largest = []
    for i in range(le):
        for j in range(le):
            for k in range(1,1+min(le-i,le-j)):
                o = [board[l][j:j+k] for l in range(i,i+k)]
                o = list(set(itertools.chain.from_iterable(o)))
                if len(o) > 1:
                    break
                if o[0] == '#':
                    break
                largest.append(k)
    return max(largest)

n = int(read(0))
for i in range(n):
    d = [str(read(0)) for j in range(int(read(0)))]
    print(solve(d))
