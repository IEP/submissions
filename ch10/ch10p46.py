#!/bin/python
def mapper(x):
    return list(map(int, x))

def swap(P,x,Q,y):
    global A
    P = pivot(P)
    Q = pivot(Q)
    t = A[P][int(x)-1]
    A[P][int(x)-1] = A[Q][int(y)-1]
    A[Q][int(y)-1] = t

def pivot(x):
    if x == 'A':
        return 0
    elif x == 'B':
        return 1

n = int(input())
A = []
for i in range(2):
    A.append(mapper(input().split()))

m = int(input())
for i in range(m):
    c = input().split()
    swap(c[0], c[1], c[2], c[3])

for i in range(2):
    o = ''
    for j in range(n):
        o += str(A[i][j])
        if j < n-1:
            o += ' '
    print(o)
