n = int(input())
winner = set()
loser = set()
for i in range(n):
    w,l = input().split()
    winner.add(w)
    loser.add(l)
winner = winner - loser
print(sorted(winner))