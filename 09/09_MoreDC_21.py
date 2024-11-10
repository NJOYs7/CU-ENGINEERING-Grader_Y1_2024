def factor(N): # N เป็ นจ ำนวนเต็มบวกมำกกว่ำ 1
    k = 1
    fc = []
    while N != 1:
        k += 1
        n = 0
        while N%k == 0:
            N = N/k 
            n += 1
        if n != 0:
            fc.append([k,n])
    return fc
        
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
