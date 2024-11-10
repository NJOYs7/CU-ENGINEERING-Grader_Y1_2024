Cards = input().split()
N = int(len(Cards)/2)
Command = input()
for i in Command:
    if i == "C":
        Cards1 = Cards[0:N]
        Cards2 = Cards[N:]
        Cards = Cards2 + Cards1
    if i == "S":
        Cards1 = Cards[0:N]
        Cards2 = Cards[N:]
        Cards = []
        for i in range(N):
            Cards.append(str(Cards1[i]))
            Cards.append(str(Cards2[i]))
Cards = " ".join(Cards)
print(Cards)