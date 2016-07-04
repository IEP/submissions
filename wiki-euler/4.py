#!/usr/bin/env python3
def pal():
    res = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            temp = i*j
            if str(temp) == str(temp)[::-1]:
                res = max(res,temp)
    return res
print(pal())
