#!/bin/python
def mapper(x):
    return list(map(int,x))
def jarak(si,sj,d):
    return abs(sj[0]-si[0])**d + abs(sj[1]-si[1])**d
p = []
dist = []
a = mapper(input().split())
for i in range(a[0]):
    p.append(mapper(input().split()))
for i in range(a[0]):
    for j in range(i+1,a[0]):
        if i == j:
            break
        else:
            dist.append(jarak(p[i],p[j],a[1]))
dist.sort()
print('{} {}'.format(dist[0], dist[len(dist)-1]))
