n = int(input())
time = {}
for i in range(n):
        song,singer,genre,t = [e.strip() for e in input().split(',')]
        m,s = [int(e) for e in t.split(':')]
        if genre not in time:
            time[genre] = 0
        time[genre] += m*60 + s
x = [(t,g) for g,t in time.items()]
x.sort()
for t,g in x[-3:][::-1]:
    m = str(t//60)
    s = ('0'+str(t%60))[-2:]
    print(g,'-->',m+':'+s)