Password = input().strip()
OK = True
#case1
if len(Password) < 8:
    print('Less than 8 characters')
#case2
UC = False
LC = False
SC = False
NC = False
for i in Password:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        UC = True
    if i in 'abcdefghijklmnopqrstuvwxyz':
        LC = True
    if i in '!@#$%^&*()_+\"':
        SC = True
    if i in '1234567890':
        NC = True
    if UC == LC == SC == NC == True:
        break
if LC == False:
    OK = False
    print('No lowercase letters')
if UC == False:
    OK = False
    print('No uppercase letters')
if NC == False:
    OK = False
    print('No numbers')
if SC == False:
    OK = False
    print('No symbols')
#case3
CR = True
c = 1
for i in range(len(Password)-1):
    if Password[i] == Password[i+1]:
        c += 1
        if c == 4:
            CR = False
            break
    else:
        c = 1
if CR == False:
    OK = False
    print('Character repetition')
#case4
NS = True
LS = False
KP = False
for i in range(len(Password)-3):
    if Password[i:i+4] in '01234567890':
        NS = False
    if Password[i:i+4] in '09876543210':
        NS = False
    if Password[i:i+4].lower() in 'abcdefghijklmnopqrstuvwxyz' or Password[i:i+4].lower() in 'zyxwvutsrqponmlkjihgfedcba':
        LS = True
    if Password[i:i+4].upper() in 'QWERTYUIOPASDFGHJKLZXCVBNMNBVCXZLKJHGFDSAPOIUYTREWQ!@#$%^&*()_++_)(*&^%$#@!':
        KP = True
if NS == False:
    OK = False
    print('Number sequence')
if LS:
    OK = False
    print('Letter sequence')
if KP:
    OK = False
    print('Keyboard pattern')
if OK:
    print('OK')
