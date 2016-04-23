#!/bin/python
def read(mode=2):
    inp = input().strip()
    if mode == 0: return inp
    if mode == 1: return inp.split()
    if mode == 2: return list(map(int,inp.split()))
N = []
data = {}
while True:
    try:
        temp = read(1)
        N.append(int(temp[1]))
        for i in range(16):
            temp = read(1)
            data[' '.join(temp[0:2])] = data.get(' '.join(temp[0:2]), []) + [temp[2]]
    except EOFError:
        break
#print(data)
data = list(data.items())
data.sort(key=lambda x: x[1])
print('N'.ljust(14) +  ' '.join(map(lambda x: str(x).rjust(5),N)))
for i in data:
    print(i[0][0:14].ljust(14) + ' '.join(map(lambda x: str(x).rjust(5),i[1])))
