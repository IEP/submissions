#!/bin/python
def mapper(x):
    return list(map(int, x))
q = mapper(input().split())
# 1st matrices
A = []
for i in range(q[0]):
    t = mapper(input().split())
    A.append(t)
# 2nd matrices
B = []
for i in range(q[1]):
    t = mapper(input().split())
    B.append(t)
# multiply
C = []
for i in range(q[0]):
    temp = []
    for j in range(q[2]):
        t = 0
        for k in range(q[1]):
            t += A[i][k] * B[k][j]
        temp.append(t)
    C.append(temp)
# output
for i in range(q[0]):
    o = ''
    for j in range(q[2]):
        o += str(C[i][j])
        if j < q[2]-1:
            o += ' '
    print(o)
