Amount = int(input())
Point = []
for i in range(Amount):
    j,k = input().split()
    j = float(j)
    k = float(k)
    d = (j*j + k*k)**0.5
    Point.append([d,i+1,j,k])
    Point.sort()
d,i,x,y = Point[2]
print("#"+str(i)+": ("+str(x)+","+" "+str(y)+")")