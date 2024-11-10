def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if e in t[i]:
            return i
    return -999
def flatten(t): # return a list of ints converted from list of lists of ints t
    flat = []
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 0:
                flat.append(t[i][j])
    return flat
def inversions(x): # return the number of inversions of list x
    inv = 0
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                inv += 1
    return inv
def solvable(t):
    PB = False
    if len(t) % 2 == 0: #even
        if inversions(flatten(t)) % 2 == 0: #inv even
            if row_number(t,0) % 2 != 0: #rn odd
                PB = True
        else: # inv odd
            if row_number(t,0) % 2 == 0: #rn even
                PB = True
    else: #odd
        if inversions(flatten(t)) % 2 == 0: #inv even
            PB = True
    return PB
exec(input().strip()) # do not remove this line
