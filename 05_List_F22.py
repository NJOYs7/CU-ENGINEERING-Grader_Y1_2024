def index_of(grades, ID):
    for e in range(len(grades)):
        i = -1
        if grades[e][0] == ID:
            i = grades.index(grades[e])
            break
    return i 
def upgrade(grades, IDs):
    G = ['F','D','D+','C','C+','B','B+','A']
    for k in IDs:
        for e in range(len(grades)):
            if grades[e][0] == k:
                k = G.index(grades[e][1]) 
                if grades[e][1] != 'A':
                    grades[e][1] = G[k+1]
    grades.sort()
# DON'T remove the following three lines
exec(input())
exec(input())
exec(input())