ids = []
grades = []
i = input().split()
G = ['F','D','D+','C','C+','B','B+','A']
while 'q' not in i:
    ids.append(i[0])
    grades.append([i[1]])
    i = input().split()
uids = input().split()
for i in uids:
    N = ids.index(i)
    grades[N] = "".join(grades[N])
    k = G.index(grades[N])
    if grades[N] != 'A':
        grades[N] = G[k+1]
for e in range(len(ids)):
    print(str(ids[e]),str("".join(grades[e])))