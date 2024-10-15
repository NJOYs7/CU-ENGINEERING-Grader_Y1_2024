DNA_Chain = input().strip().upper()
is_Invalid = False
for i in DNA_Chain:
    if i not in 'ATGC':
        is_Invalid = True
if is_Invalid:
    print("Invalid DNA")
Operator = input()
#R
if not is_Invalid:
    if Operator == 'R':
        R_complement = ''
        for i in DNA_Chain:
            if i == 'A':
                R_complement += 'T'
            if i == 'T':
                R_complement += 'A'
            if i == 'G':
                R_complement += 'C'
            if i == 'C':
                R_complement += 'G'
        R_complement = R_complement[-1::-1]
        print(R_complement)
    #F
    if Operator == 'F':
        c_A = 0 ; c_T = 0 ; c_G = 0 ; c_C = 0
        for i in DNA_Chain:
            if i == 'A':
                c_A += 1
            if i == 'T':
                c_T += 1
            if i == 'G':
                c_G += 1
            if i == 'C':
                c_C += 1
        print('A='+str(c_A)+',','T='+str(c_T)+',','G='+str(c_G)+',','C='+str(c_C))
    #D
    if Operator == 'D':
        Pattern = str(input()).strip()
        c = 0
        for i in range(len(DNA_Chain)-1):
            x = DNA_Chain[i] + DNA_Chain[i+1]
            if x == Pattern:
                c += 1
        print(c)