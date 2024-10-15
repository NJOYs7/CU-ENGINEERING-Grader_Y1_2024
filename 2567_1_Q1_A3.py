n = int(input())
c = n
line = []
while n != 0:
    line.append(input().strip())
    n -= 1
func = input()
# rot 90
if func == 'rot90':
    x = ''
    for i in line[::-1]:
        x += i
    for i in range(len(line[0])):
        print(x[i::len(line[0])])
# rot 180
if func == 'rot180':
    for i in line[::-1]:
        print(i[::-1])


#@@@@@@@@..@@.....@.@@.....@.@@@@@@@..@@.......@@.......@@......
# .....@@@@......@@.......@@.......@@..@@@@@@@.@.....@@.@.....@@..@@@@@@@@