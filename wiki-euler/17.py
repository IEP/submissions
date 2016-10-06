#!/usr/bin/env python3
def spellCount(n):
    res = 0
    d = [(1,'one'),(2,'two'),(3,'three'),
         (4,'four'),(5,'five'),(6,'six'),
         (7,'seven'),(8,'eight'),(9,'nine'),
         (10,'ten'),(11,'eleven'),(12,'twelve'),
         (13,'thirteen'),(14,'fourteen'),(15,'fifteen'),
         (16,'sixteen'),(17,'seventeen'),(18,'eighteen'),
         (19,'nineteen')]
    e = [(20,'twenty'),(30,'thirty'),(40,'forty'),
         (50,'fifty'),(60,'sixty'),(70,'seventy'),
         (80,'eighty'),(90,'ninety')]
    if n == 1000:
        res += len('onethousand')
    elif 100 <= n < 1000:
        res += 7
        temp = n//100
        if n % 100 != 0:
            res += 3
        for i in d[:10]:
            if temp == i[0]:
                res += len(i[1])
                n -= temp * 100
                break
    if n >= 20:
        temp = n//10
        for i in e:
            if temp * 10 == i[0]:
                res += len(i[1])
                n -= temp * 10
                break
    if 1 <= n < 20:
        for i in d:
            if n == i[0]:
                res += len(i[1])
                break
    return res
counting = 0
for i in range(1,1001):
    temp = spellCount(i)
    counting += temp
    print(i,temp)
print(counting)
