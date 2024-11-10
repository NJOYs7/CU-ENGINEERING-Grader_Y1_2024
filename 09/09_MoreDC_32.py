def first_fit(L, e):
    for i in range(len(L)):
        n = 0
        for j in range(len(L[i])):
            n += L[i][j]
        if n + e <= 100:
            L[i].append(e)
            return
    L.append([e])
def best_fit(L, e):
    bf = [0,0,True]
    for i in range(len(L)):
        n = 0
        for j in range(len(L[i])):
            n += L[i][j]
        if n + e <= 100:
            if bf[0] < n+e:
                bf[0] = n+e
                bf[1] = i
                bf[2] = False
    if bf[2]:
        L.append([e])
    else:
        L[bf[1]].append(e)

def partition_FF(D):
    L = []
    for x in D:
        first_fit(L,x)
    return L
def partition_BF(D):
    L = []
    for x in D:
        best_fit(L,x)
    return L
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ