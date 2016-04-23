#!/bin/python
def replacer(s):
    s = str(s)
    temp = ''
    for i in s:
        if i == '1':
            temp += 'L'
        else:
            temp += 'G'
    return temp
n = int(input())
# 0 = G, 1 = L
seq = [replacer(bin(i)[2:].zfill(n)) for i in range(2**n)]
print(seq)
