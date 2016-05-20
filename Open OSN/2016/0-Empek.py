#!/usr/bin/env python3
res = 0
def dfs(a,b):
    global res, n
    if b == 3:
        res += 1
    else:
        for i in range(a+1,n):
            if m[i] == b+1:
                dfs(i,b+1)
subtask = input()
n = int(input())
m = list(map(int,input()))
for i in range(n):
    if m[i] == 1:
        dfs(i,1)
print(res)
