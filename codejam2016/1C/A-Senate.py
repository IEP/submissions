#!/usr/bin/env python3
for T in range(int(input())):
    N = int(input())
    d = list(map(int,input().split()))
    total = sum(d)
    population = {}
    for i in range(N):
        population[chr(ord('A')+i)] = d[i]
    out = []
    while total > 0:
        temp = ''
        population1 = list(population.items())
        population1.sort(key=lambda x: x[1], reverse = True)
        for i, j in population1:
            if len(temp) == 1:
                break
            if j > 0:
                temp += i
                population[i] -= 1
                total -= 1
        out.append(temp)
    out1 = ''
    temp = ''
    for i in out:
        if len(temp) == 2:
            out1 += ' '
            temp = ''
        temp += i
        out1 += i
    print('Case #{}: {}'.format(T+1,out1))
