#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))

n = read()
demand = n[1]
# 0 = W, 1 = C
temp = [read() for i in range(2)]
d = [[temp[0][i],temp[1][i]] for i in range(n[0])]
# sort by net price
d.sort(key=lambda x: x[1]/x[0], reverse=True)
t = 0.0
for i in range(n[0]):
    if demand <= 0.0:
        break
    else:
        # C/W
        net = d[i][1]/d[i][0]
        weight = d[i][0]
        t += min(weight,demand) * net
        demand -= min(weight,demand)
print('{:.5f}'.format(t))
