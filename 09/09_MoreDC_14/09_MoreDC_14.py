cid = {}
f = open(input().strip())
for line in f:
    ID,course = [e.strip() for e in line.split(',')]
    cid[ID] = course
f.close()
tid = {}
f = open(input().strip())
for line in f:
    ID,teacher = [e.strip() for e in line.split(',')]
    tid[ID] = teacher
f.close()
f = open(input().strip())
for line in f:
    course,teacher = [e.strip() for e in line.split(',')]
    if course in cid and teacher in tid:
        print(cid[course]+','+tid[teacher])
    else:
        print('record error')