def less_check(sid1,sid2):
    if sid1[-2::] < sid2[-2::]:
        return True
    elif sid1[-2::] > sid2[-2::]:
        return False
    else:
        return sid1 < sid2
def read_next(f):
    t = f.readline()
    if len(t) == 0:
        return ['' , '']
    return t.strip().split()

filename1,filename2 = input().split()
fin1 = open(filename1,'r')
fin2 = open(filename2,'r')
sid1,g1 = read_next(fin1)
sid2,g2 = read_next(fin2)

while sid1 != '' and sid2 != '':
    if less_check(sid1,sid2):
        print(sid1,g1)
        sid1,g1 = read_next(fin1)
    else:
        print(sid2,g2)
        sid2, g2 = read_next(fin2)
while sid1 != '':
    print(sid1, g1)
    sid1, g1 = read_next(fin1)
while sid2 != '':
    print(sid2, g2)
    sid2, g2 = read_next(fin2)
fin1.close()
fin2.close()
