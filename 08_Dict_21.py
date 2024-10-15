# นับจำนวนของตัวอักษร
from itertools import count

char = input().lower()
COUNT = { }
for i in char:
    if 'a' <= i <= 'z':
        if i in COUNT:
            COUNT[i] += 1
        else :
            COUNT[i] = 1
x = []
for e in COUNT:
    x.append([-COUNT[e],e])
x.sort()
for c in x:
    print(c[1],'->',-c[0])
