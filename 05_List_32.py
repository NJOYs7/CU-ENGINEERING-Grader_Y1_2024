q = list()
sum_qtime = 0
n_custumer = 0
n = int(input())
for i in range(n):
    c = input().split()
    if c[0] == 'reset':
        ticketID = int(c[1])
    elif c[0] == 'new':
        t = int(c[1])
        q.append([ticketID,t])
        print('ticket',ticketID)
        ticketID += 1
    elif c[0] == 'next':
        nextid, qt = q.pop(0)
        print("call",nextid)
    elif c[0] == 'order':
        odt = int(c[1])
        dt =  odt - qt
        print("qtime",nextid,dt)
        n_custumer += 1
        sum_qtime += dt
    elif c[0] == 'avg_qtime':
        avg = sum_qtime / n_custumer
        print( "avg_qtime", round(avg,4) )