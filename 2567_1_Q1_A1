a, b, c, d = [int(i) for i in input().split()]

if a == 1:
    a = b+c+d
    if b > 4:
        c += c*d
        if b > 5:
            c += c%d
        else:
            c += c//d
    elif b > 5:
        c += c%d
    elif b == 2:
        c += c-d
    elif b == 1:
        c += c+d
    else:
        c += c//d
    print(c)
else:
    while b < c:
        b += 1  
        if b <= a:
            c -= 1 
            if a > d:
                break 
            elif a <= d:
                a += c
        else:
            break

print(a, b, c, d)

