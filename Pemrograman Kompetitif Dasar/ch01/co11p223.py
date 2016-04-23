#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
def scan(wts):
    res = []
    for i in range(len(wts)):
        temp = set(wts[i])
        if len(temp) == 1 and list(temp)[0] == 1:
            res.append(i)
    if len(res) > 0:
        return True, res
    else:
        return False, 0
R, C = read()
data = [[int(j) for j in read(0)] for i in range(R)]
while True:
    temp = scan(data)
    if temp[0]:
        for i in temp[1]:
            data[i] = [0] * C
        pivot = temp[1][-1]
        # print('pivot',pivot)
        for i in range(C):
            for j in range(pivot,R):
                # print('looping..')
                if data[j][i] == 1 or j == R - 1:
                    # memo j as limit
                    # print(j,i,data[j][i])
                    if j == R - 1:
                        j = R
                    part = [data[k][i] for k in range(j)]
                    # print(part)
                    for k in range(j):
                        data[k][i] = 0 if k < len(part) - part.count(1) else 1
                    break
        # print('step')
        # for i in data:
        #     print(''.join(map(str,i)))
    else:
        break
# print('end')
for i in data:
    print(''.join(map(str,i)))
