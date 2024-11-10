def make_int_list(x):
    x = [int(e) for e in x.split()]
    return x

def is_odd(e):
    return e % 2 != 0

def odd_list(alist):
    a_list = []
    for e in alist:
        if is_odd(e):
            a_list.append(e)
    return a_list

def sum_square(alist):
    total_sum = 0
    for e in alist:
        total_sum += e ** 2  # Corrected this line
    return total_sum

exec(input().strip()) 
