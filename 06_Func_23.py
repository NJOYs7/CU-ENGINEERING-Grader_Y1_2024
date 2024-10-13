def make_int_list(x):
    x = [int(e) for e in x.split()]
    return x
def is_odd(e):
 if e % 2 != 0:
    return True
 else:
    return False
def odd_list(alist):
   a_list = []
   for e in range(len(alist)):
      x = is_odd(alist[e])
      if x == True:
         a_list.append(alist[e])
    return alist

def sum_square(alist):
   Sum = 0
   for e in alist:
      Sum += int(alist)**2
    return Sum

exec(input().strip()) 
