n = int(input())
for j in range(n):
    Line = input()
    c = 0
    for k in Line:
        if k == '.':
            c += 1
        else:
            if c > 0:
                Line = Line[c//2:len(Line)]
            print(Line)
            break