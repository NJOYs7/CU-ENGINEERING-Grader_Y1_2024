def gcd(a,b):
     while b != 0:
         a,b = b, a%b
     return a
def is_coprime(a, b, c):
    co_prime = True
    if gcd(a,b) != 1:
        if gcd(b,c) != 1:
            co_prime = False
    return co_prime
def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(3,max_len+1):
        for a in range(3,c):
            for b in range(a,c+1):
                if a**2+b**2 == c**2 and is_coprime(a,b,c):
                    triple.append([a,b,c])
    return triple
exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ