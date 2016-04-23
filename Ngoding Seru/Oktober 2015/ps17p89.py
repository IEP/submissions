#!/bin/python
s = str(input())
angka = [str(i) for i in range(10)]
hurufKecil = [chr(i) for i in range(ord('a'),ord('z')+1)]
hurufBesar = [chr(i) for i in range(ord('A'),ord('Z')+1)]
special = ['_', '!', '?']
flag = [0, 0, 0, 0]
huruf = 0
for i in s:
    if i in angka:
        flag[0] = 1
    elif i in hurufKecil:
        flag[1] = 1
        huruf += 1
    elif i in hurufBesar:
        flag[2] = 1
        huruf += 1
    elif i in special:
        flag[3] = 1
if len(s) >= 8 and sum(flag) == 4:
    o = 'Kuat'
elif huruf > 12:
    o = 'AgakKuat'
else:
    o = 'Lemah'
print(o)
