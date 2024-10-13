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

sort_data = []
for j in range(len(ids)):
    sort_data.append([ids[j],"".join(grades[j])])
    sort_data.sort()

for e in range(len(ids)):
    print(str(sort_data[e][0]),str(sort_data[e][1]))