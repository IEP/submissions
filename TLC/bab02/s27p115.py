#!/usr/bin/env python3
A, op, B = input().split()
A, B = map(int,(A,B))
if op == '+':
    print(A+B)
elif op == '-':
    print(A-B)
elif op == '*':
    print(A*B)
elif op == '<':
    print('benar' if A < B else 'salah')
elif op == '>':
    print('benar' if A > B else 'salah')
elif op == '=':
    print('benar' if A == B else 'salah')
