Data = input()
Result = ''
for i in Data:
    if '0' <= i <= '9' or  'a' <= i.lower() <= 'z':
        Result += i
    else:
        Result += ' '
Result = Result.split()
Camel = ''
Camel = Camel + (Result[0].lower())
for i in range(1,len(Result)):
    Result[i] = Result[i][0].upper() + Result[i][1:].lower()
    Camel = Camel + Result[i]
print(Camel)