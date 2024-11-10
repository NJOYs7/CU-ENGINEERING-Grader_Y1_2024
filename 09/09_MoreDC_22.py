def read_matrix():
     m = []
     nrows = int(input())
     for k in range(nrows):
         x = input().split()
         r = []
         for e in x:
             r.append( float(e) )
         m.append(r)
     return m
def mult_c(c, A):
    for j in range(len(A)):
        for k in range(len(A[j])):
            A[j][k] = float(A[j][k])*c
    return A      
def mult(A, B):
    rA = len(A)
    cA = len(A[0])
    rB = len(B)
    cB = len(B[0])
    C = [[0]*cB for k in range(rA)]
    for i in range(rA):
        for j in range(cB):
            C[i][j] = 0
            for k in range(cA):
                C[i][j] += A[i][k]*B[k][j]
    return C
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ