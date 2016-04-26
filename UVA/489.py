#!/bin/python
while True:
    round = int(input())
    if round == -1:
        break
    s = input()
    a = input()
    s, a = list(s), list(a)
    for i in range(min(7,len(a))):
        while a[i] in s:
            s.remove(a[i])
    s = ''.join(s)
    if len(s) == 0:
        print('Round {}\nYou win.'.format(round))
    elif len(s) > 0 and len(a) > 7:
        print('Round {}\nYou lose.'.format(round))
    else:
        print('Round {}\nYou chickened out.'.format(round))
