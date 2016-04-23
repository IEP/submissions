#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
T = int(read(0))
for i in range(T):
    N = int(read(0))
    d = read()
    graph = {}
    for j in range(len(d)):
        graph[j+1] = set([d[j]])
    for j in range(len(d)):
        a, b = j+1, list(graph[j+1])[0]
        graph[b] |= set([a])
    #print(graph)
    o = []
    p = []
    for j in range(len(d)):
        o.append(dfs(graph,j+1))
    print('case',i+1)
    dfsMax = 0
    for j in o:
        temp = len(j)
        if temp > dfsMax:
            dfsMax = temp
            p.append(j)
    print(p)
