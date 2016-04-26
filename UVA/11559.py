#!/bin/python
def pecah(x):
    return list(map(int,x.split()))
while True:
    try:
        n, b, h, w = pecah(input())
        cheapest = -1
        for i in range(h):
            price = int(input())
            slot = pecah(input())
            for j in slot:
                if j > n:
                    if cheapest == -1 or price < cheapest:
                        cheapest = price
        net = cheapest * n
        if net < b:
            print(net)
        else:
            print('stay home')
    except EOFError:
        break
