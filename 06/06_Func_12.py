def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    while True:
        N += 1
        if is_prime(N) == True:
            break
    return N
def next_twin_prime(N):
    while True:
        A = next_prime(N)
        B = next_prime(A)
        if B - A == 2:
            break
        else:
            N += 1
    return (A, B) 

exec(input().strip())