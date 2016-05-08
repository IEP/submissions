#!/bin/python
a = input()
b = input()
flag = False
o = 'Tentu saja bisa!'
if len(a) == len(b)+1:
    b += ' '
    for i in range(len(a)):
        if not (a[i] == b[i] or a[i] == b[i-1]):
            if not flag:
                flag = True
            else:
                o = 'Wah, tidak bisa :('
else:
    o = 'Wah, tidak bisa :('
print(o)
