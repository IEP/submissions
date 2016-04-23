#!/bin/python
def m(x):
    return list(map(int,x))
a = m(input().split())
p = []
atas = -1
bawah = -1
for i in range(a[0]):
    p.append(m(input().split()))
for i in range(a[0]):
    for j in range(i+1,a[0]):
        d = abs(p[j][1]-p[i][1])**a[1] + abs(p[j][0]-p[i][0])**a[1]
        if atas == -1 or bawah == -1:
            atas = d
            bawah = d
        else:
            if d > atas:
                atas = d
            if d < bawah:
                bawah = d
print('{} {}'.format(bawah, atas))
