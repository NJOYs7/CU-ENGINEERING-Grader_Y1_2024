a,b = input().split() ; a = int(a,2) ; b = int(b,2)
a += b ; a = bin(a)
print(a[2:])
