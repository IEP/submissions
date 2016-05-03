#!/usr/bin/env python3
T = int(input())
for i in range(T):
    switch = False
    C, J = map(list,input().split())
    for j in range(len(C)):
        if C[j] != '?':
            C[j] = int(C[j])
        if J[j] != '?':
            J[j] = int(J[j])
        if not switch:
            if C[j] == J[j] == '?':
                C[j] = J[j] = 0
            elif C[j] == '?':
                C[j] = J[j]
            elif J[j] == '?':
                J[j] = C[j]
        elif isinstance(C[j],int) and isinstance(J[j],int) and not(switch):
            switch = True
            if C[j] > J[j]:
                mode = 0
            elif C[j] < J[j]:
                mode = 1
            else:
                mode = 2
        else:
            if C[j] == J[j] == '?':
                if mode == 0:
                    C[j] = 0
                    J[j] = 9
                elif mode == 1:
                    C[j] = 0
                    J[j] = 9
    print(C,J)
