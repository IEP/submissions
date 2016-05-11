#!/usr/bin/env python3
for T in range(1,int(input())+1):
    J, P, S, K = map(int,input().split())
    temp = []
    for i in range(1,J+1):
        for j in range(1,P+1):
            counter = 1
            for k in range(1,S+1):
                if counter <= K:
                    temp.append((i,j,k))
                    counter += 1
                else:
                    counter = 0
                    break
    print('Case #{}: {}'.format(T,len(temp)))
    for i,j,k in temp:
        print('{} {} {}'.format(i,j,k))
