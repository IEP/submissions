#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mdoe == 2: return list(map(int,inp.split()))
s = read(0)
N = int(read(0))
d = [read(0)[0:100] for i in range(N)]
o = []
if s != '*':
    wtf = s.split('*')
    if len(wtf[0]) > 0 and len(wtf[1]) == 0:
        o = [i for i in d if i.startswith(wtf[0])]
    elif len(wtf[0]) == 0 and len(wtf[1]) > 0:
        o = [i for i in d if i.endswith(wtf[1])]
    else:
        o = [i for i in d if i.startswith(wtf[0]) and i.endswith(wtf[1])]
else:
    o = d
if len(o) > 0:
    print('\n'.join(o))
