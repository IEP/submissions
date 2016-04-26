#!/usr/bin/env python3
while True:
    try:
        n = int(input())
        if 1 <= n < 10:
            print('satuan')
        elif 10 <= n < 100:
            print('puluhan')
        elif 100 <= n < 1000:
            print('ratusan')
        elif 1000 <= n < 10000:
            print('ribuan')
        elif 10000 <= n < 100000:
            print('puluhribuan')
    except EOFError:
        break
