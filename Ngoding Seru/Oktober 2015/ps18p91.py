#!/bin/python
detik = int(input())
jam = detik//3600
detik -= jam*3600
menit = detik//60
detik -= menit*60
print(jam)
print(menit)
print(detik)
