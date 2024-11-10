Cartoon = {}
Animals = []
while True:
    data = input()
    if 'q' in data : break
    Name, Animal = [e.strip() for e in data.split(',')]
    if Animal not in Cartoon:
        Cartoon[Animal] = []
        Animals.append(Animal)
    Cartoon[Animal].append(Name)
    
for i in Animals:
    print(i+':',', '.join(Cartoon[i]))