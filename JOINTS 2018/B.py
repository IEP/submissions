#!/usr/bin/env python2
for T in range(1, int(raw_input()) + 1):
    N, M = list(map(int, raw_input().split()))
    # print(N, M)
    semut = [i for i in range(1, N+1)]
    # print(semut)
    depth = list(map(int, raw_input().split()))
    # print(depth)
    for i in depth:
        # semut = semut[:i] + semut[i+1:]
        semut = semut[i:] + semut[:i][::-1]
        #print(semut)
    print('Kasus #{}: {}'.format(T, ' '.join(map(str, semut))))