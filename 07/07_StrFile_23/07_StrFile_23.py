filename , year = input().split()
y = year[-2:]
fin = open(filename,"r")
d = []
for line in fin:
    line = line.split()
    s_y = line[0][0:2]
    if s_y == y:
        d.append(float(line[1]))
if len(d) == 0:
    print("No data")
else:
    print(min(d),max(d),sum(d)/len(d))
