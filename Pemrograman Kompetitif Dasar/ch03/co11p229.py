#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
N, temp = read()
A = [read() for i in range(N)]
M, temp = read()
B = [read() for i in range(N)]
if A == B:
    print('identik')
elif A == B[::-1]:
    print('horizontal')
elif A == [i[::-1] for i in B]:
    print('vertikal')
elif A == list(map(list,list(zip(*B)))):
    print('diagonal kanan bawah')
elif A == [i[::-1] for i in map(list,list(zip(*B))[::-1])]:
    print('diagonal kiri bawah')
else:
    print('tidak identik')
