#!/usr/bin/env python3
d = [list(map(int,input().split())) for i in range(20)]
res = 0
for i in range(20):
    for j in range(20):
        # right
        if j < 16:
            td = [d[i][j+x] for x in range(4)]
            tr = 1
            for k in td:
                tr *= k
            res = max(res,tr)
        # down
        if i < 16:
            td = [d[i+x][j] for x in range(4)]
            tr = 1
            for k in td:
                tr *= k
            res = max(res,tr)
        # diag left
        if i < 16 and j < 16:
            td = [d[i+x][j+x] for x in range(4)]
            tr = 1
            for k in td:
                tr *= k
            res = max(res,tr)
        # diag right
        if i < 16 and j >= 4:
            td = [d[i+x][j-x] for x in range(4)]
            tr = 1
            for k in td:
                tr *= k
            res = max(res,tr)
print(res)
