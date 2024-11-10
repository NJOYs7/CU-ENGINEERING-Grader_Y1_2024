Anagram1 = input().lower()
Anagram2 = input().lower()
Ana1 = ''
Ana2 = ''
for i in Anagram1:
    if 'a' <= i <= 'z':
        Ana1 = Ana1 + i
for i in Anagram2:
    if 'a' <= i <= 'z':
        Ana2 = Ana2 + i
is_ana = True
while len(Ana1) > 0:
    c = Ana1[0]
    k = Ana2.find(c)
    if k == -1:
        is_ana = False
        break
    Ana1 = Ana1[1:]
    Ana2 = Ana2[:k] + Ana2[k+1:]
if Ana1 != '' or Ana2 != '':
    is_ana = False
if is_ana:
    print("YES")
else:
    print("NO")