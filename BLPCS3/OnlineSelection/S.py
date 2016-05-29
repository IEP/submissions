#!/usr/bin/env python3
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
d = ["####..#.....",
     "#...#.#.....",
     "#...#.#.....",
     "####..#.....",
     "#...#.#.....",
     "#...#.#.....",
     "####..#####.",
     "............"]
R, C = read()
for i in range(R):
    if i == 0:
        print('.' + ''.join(["............"] * C))
    for j in range(len(d)):
        print('.' + ''.join([d[j]] * C))
