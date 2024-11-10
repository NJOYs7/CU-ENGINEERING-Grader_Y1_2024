# ( USING LIST )
# Word = str(input())
# o = [Word]
# # s,x,ch -> es
# if Word[-1] in ['s','x'] or Word[-2:] == 'ch':
#     o.append('es')
    
# y -> i+es
# elif Word[-1] == 'y':
#     if Word[-2] not in ['a','e','i','o','u']:
#         o.append('ies')
#         o[0] = Word[0:-1]
#     else:
#         o.append('s')   
# # -> s
# else:
#     o.append('s')
# Word = "".join(o)
# print(Word)

# ( USING STRING ONLY )
Word = str(input())
# s,x,ch -> es
if Word[-1] in ['s','x'] or Word[-2:] == 'ch':
    Word = Word + 'es'
# y -> i+es
elif Word[-1] == 'y':
    if Word[-2] not in ['a','e','i','o','u']:
        Word = Word[0:-1] + 'ies'
    else:
        Word = Word + 's'
# -> s
else:
    Word = Word + 's'
print(Word)