n = int(input())
S = []
U = set()
L = []
for i in range(n):
    L = input().split()
    S.append(set(L))
I = set(L)
for i in S:
    s = set(i)
    U = U.union(s)
    I = I.intersection(s)
print(len(U),'\n'+str(len(I)))