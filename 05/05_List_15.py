d = []
data = input().split()
data = [int(e) for e in data] 
for i in data:
    if i not in d:
        d.append(i)
c = len(d)
d = sorted(d)
print(c)
print(d[0:10])