def pattern1(nrows, ncols):
    P1 = []
    n = 0
    for i in range(nrows):
        p1 = []
        for j in range(ncols):
            n += 1
            p1.append(n)
        P1.append(p1)
    return P1
def pattern2(nrows, ncols):
    P2 = []
    for i in range(1,nrows+1):
        p2 = []
        for j in range(ncols):
            p2.append(i)
            i += nrows
        P2.append(p2)
    return P2
def pattern3( N ):
    P3 = []
    n = 0
    for i in range(N):
        p3 = []
        if i > 0:
            for j in range(i):
                p3.append(0)
        for k in range(N-i):
            n += 1
            p3.append(n)
        P3.append(p3)
    return P3
def pattern4( N ):
    P4 = [[0]*N for i in range(N)]
    i = 1
    for c in range(N):
        for r in range(c,-1,-1):
            P4[r][c] = i
            i += 1
    return P4
def pattern5( N ):
    x = [[0]*N for i in range(N)]
    i = 1
    for d in range(N):
        for r in range(0,N-d):
            c = r + d
            x[r][c] = i
            i += 1
    return x
def pattern6( N ):
    x = [[0]*N for i in range(N)]
    i = 1
    for d in range(N):
        if d%2 == 0:
            for r in range(0,N-d):
                c = r + d
                x[r][c] = i
                i += 1
        else:
            for r in range(N-d-1,-1,-1):
                c = r + d
                x[r][c] = i
                i += 1
    return x
#def pattern6( N ): 
exec(input().strip()) 