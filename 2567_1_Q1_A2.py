info = input().split()
Date = info[0].split("/")
Day = int(Date[0]); Month_BD = int(Date[1]); Year = int(Date[2])
Money = int(info[1])
Range = int(info[2])
Start = int(info[3])
Count = 1
Ir = 0
while Range != 0:
    #Month_Control
    if Start > 12:
        Start -= 12
    #BD_BONUS
    if Start == Month_BD:
        Ir += 1
    # Interest Rate Calculation
    if Count > 4:
        Count -= 4
    Ir += Count
    Money += Money*(Ir/100)*(1/12)
    Range -= 1
    Start += 1
    Count += 1
    Ir = 0
print(round(Money,2))
